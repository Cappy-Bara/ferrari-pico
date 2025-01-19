from device.peripherals.Heater.Plug import Plug


class Heater:

    def __init__(self, plug : Plug):
        self.is_working = False

    def start_heating(self):
        """Turns on the heater"""
        pass

    def stop_heating(self):
        """Turns off the heater"""
        pass