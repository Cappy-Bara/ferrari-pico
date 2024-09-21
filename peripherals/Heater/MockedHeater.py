from peripherals.Heater.Heater import Heater

class MockedHeater(Heater):

    def __init__(self, name):
        self.is_working = False
        self._name = name

    def start_heating(self):
        self.is_working = True
        print(f"HEATER {self._name} IS ON.")

    def stop_heating(self):
        self.is_working = False
        print(f"HEATER {self._name} IS OFF.")