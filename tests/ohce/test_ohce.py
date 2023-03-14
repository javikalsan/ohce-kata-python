from unittest import TestCase
from doublex import Stub, when

import os
import pexpect

from src.ohce.kata import Clock, OhceKata

A_NAME = "a_name"
EXIT_COMMAND = "Stop!"
LOG_FILE_PATH = "/tmp/oche_tests.log"
OCHE_BIN = "oche"


class TestOhceKataOutsideIn(TestCase):
    def setUp(self):
        project_path = os.getcwd()
        self.oche_bin = os.path.join(project_path, OCHE_BIN)
        self.oche_bin_spawned = pexpect.spawn(self.oche_bin, [A_NAME])
        self.oche_bin_spawned.logfile = open(LOG_FILE_PATH, "bw")

    def tearDown(self):
        self.oche_bin_spawned.sendline(EXIT_COMMAND)
        self.oche_bin_spawned.logfile.close()

    def assert_stdout_contains(self, expected_stdout):
        log_file_lines = []
        with open(LOG_FILE_PATH, "r") as f:
            log_file_lines = f.readlines()
        matches = [x for x in log_file_lines if expected_stdout in x]
        self.assertTrue(len(matches) > 0)

    def test_ohce_returns_greeting_with_name(self):
        self.oche_bin_spawned.expect([f"Buenas", f"{A_NAME}"])

        self.assert_stdout_contains(A_NAME)

    def test_ohce_returns_reversed_input(self):
        self.oche_bin_spawned.expect([f"Buenas", f"{A_NAME}"])
        self.oche_bin_spawned.sendline("hola")
        self.oche_bin_spawned.expect([f"aloh"])

        self.assert_stdout_contains("aloh")

    def test_ohce_returns_reversed_input_and_comment_when_palindrome(self):
        self.oche_bin_spawned.expect([f"Buenas", f"{A_NAME}"])
        self.oche_bin_spawned.sendline("oso")
        self.oche_bin_spawned.expect([f"oso", f"Bonita palabra"])

        self.assert_stdout_contains("oso")
        self.assert_stdout_contains("¡Bonita palabra!")

    def test_ohce_returns_reversed_input_until_exit_command(self):
        self.oche_bin_spawned.expect([f"Buenas", f"{A_NAME}"])
        self.oche_bin_spawned.sendline("hola")
        self.oche_bin_spawned.expect([f"aloh"])
        self.oche_bin_spawned.sendline("oso")
        self.oche_bin_spawned.expect([f"oso", f"Bonita palabra"])
        self.oche_bin_spawned.sendline("Stop!")
        self.oche_bin_spawned.expect([f"Adios"])

        self.assert_stdout_contains(f"Adios {A_NAME}")


class TestOhceKata(TestCase):
    def setUp(self):
        self.clock = Stub(Clock)
        self.sut = OhceKata(self.clock)

    def test_greeting_between_20_and_6_hours(self):
        when(self.clock).current_hour().returns(22)

        expected_greeting = f"¡Buenas noches {A_NAME}!"
        self.assertEqual(self.sut.greeting(A_NAME), expected_greeting)

    def test_greeting_between_6_and_12_hours(self):
        when(self.clock).current_hour().returns(10)

        expected_greeting = f"¡Buenos días {A_NAME}!"
        self.assertEqual(self.sut.greeting(A_NAME), expected_greeting)

    def test_greeting_between_12_and_20_hours(self):
        when(self.clock).current_hour().returns(14)

        expected_greeting = f"¡Buenas tardes {A_NAME}!"
        self.assertEqual(self.sut.greeting(A_NAME), expected_greeting)

    def test_clock_current_hour_is_int(self):
        clock = Clock()

        self.assertTrue(isinstance(clock.current_hour(), int))
