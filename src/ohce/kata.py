import datetime

EXIT_COMMAND = "Stop!"
PROMPT_PRINT_SYMBOL = "> "
PROMPT_READ_SYMBOL = "$ "
PALINDROME_COMMENT = "¡Bonita palabra!"
BYE_MESSAGE = "Adios"


class OhceKata:
    def __init__(self, clock):
        self.clock = clock
        self.interactions = 0
        self.name = None

    def print_stdout(self, text):
        print(f"{PROMPT_PRINT_SYMBOL}{text}")

    def run(self, arg):
        stdin = None
        while True:
            self.print_greeting(arg)
            stdin = input(f"{PROMPT_READ_SYMBOL}")
            if stdin == EXIT_COMMAND:
                self.print_stdout(f"{BYE_MESSAGE} {self.name}")
                break
            self.print_stdout(stdin[::-1])
            if self.is_palindrome(stdin):
                self.print_stdout(f"{PALINDROME_COMMENT}")

    def print_greeting(self, arg):
        if self.interactions == 0:
            self.name = arg
            self.print_stdout(self.greeting(self.name))
            self.interactions += 1

    def greeting(self, name):
        current_hour = self.clock.current_hour()
        if self.is_between_20_and_6_hours(current_hour):
            return f"¡Buenas noches {name}!"
        if self.is_between_6_and_12_hours(current_hour):
            return f"¡Buenos días {name}!"
        return f"¡Buenas tardes {name}!"

    def is_between_20_and_6_hours(self, current_hour):
        return current_hour >= 20 or current_hour < 6

    def is_between_6_and_12_hours(self, current_hour):
        return current_hour >= 6 and current_hour < 12

    def is_palindrome(self, text):
        return text == text[::-1]


class Clock:
    def current_hour(self):
        now = datetime.datetime.now()
        return now.hour
