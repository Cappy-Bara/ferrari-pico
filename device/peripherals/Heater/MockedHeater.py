from device.peripherals.Heater.Heater import Heater
from device.peripherals.Heater.Plug import Plug

class MockedHeater(Heater):

    def __init__(self, name, plug : Plug):
        self.is_working = False
        self._name = name
        self._plug = plug

    def start_heating(self):
        if(not self._plug.isPlugged):
            return self.stop_heating()
        self.is_working = True
        print(f"HEATER {self._name} IS ON.")

    def stop_heating(self):
        self.is_working = False
        print(f"HEATER {self._name} IS OFF.")