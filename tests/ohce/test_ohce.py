import unittest
from doublex import Stub, when

from src.ohce.kata import Clock, OhceKata


class TestOhceKata(unittest.TestCase):

    def setUp(self) -> None:
        self.a_name = "a_name"
        self.clock = Stub(Clock)
        self.sut = OhceKata(self.clock)

    def test_greeting_between_20_and_6_hours(self):
        when(self.clock).current_hour().returns(22)
        
        expected_greeting = f"¡Buenas noches {self.a_name}!"
        self.assertEqual(self.sut.greeting(self.a_name), expected_greeting)
                
    def test_greeting_between_6_and_12_hours(self):
        when(self.clock).current_hour().returns(10)

        expected_greeting = f"¡Buenos días {self.a_name}!"
        self.assertEqual(self.sut.greeting(self.a_name), expected_greeting)

    def test_greeting_between_12_and_20_hours(self):
        when(self.clock).current_hour().returns(14)

        expected_greeting = f"¡Buenas tardes {self.a_name}!"
        self.assertEqual(self.sut.greeting(self.a_name), expected_greeting)


    def test_clock_current_hour(self):
        clock = Clock()

        self.assertTrue(isinstance(clock.current_hour(), int))
