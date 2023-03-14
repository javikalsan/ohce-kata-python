import datetime

class OhceKata:
    def __init__(self, clock):
        self.clock = clock
    
    def greeting(self, name):
        current_hour = self.clock.current_hour()
        if self.is_between_20_and_6_hours(current_hour):
            return "¡Buenas noches {}!".format(name)
        if self.is_between_6_and_12_hours(current_hour):
            return "¡Buenos días {}!".format(name)
        return "¡Buenas tardes {}!".format(name)


    def is_between_20_and_6_hours(self, current_hour):
        return current_hour >= 20 or current_hour < 6
    
    def is_between_6_and_12_hours(self, current_hour):
        return current_hour >= 6 and current_hour < 12


class Clock:
    def current_hour(self):
        now = datetime.datetime.now()
        return now.hour
