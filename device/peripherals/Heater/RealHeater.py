from device.peripherals.Heater.Heater import Heater
from device.peripherals.Heater.Plug import Plug
import machine

class RealHeater(Heater):

    def __init__(self, heaterPin:int, plug : Plug):
        self.is_working = False
        self._plug = plug
        self._pin = machine.Pin(heaterPin, machine.Pin.OUT)

    def start_heating(self):
        if(not self._plug.isPlugged):
            return self.stop_heating()

        self.is_working = True
        self._pin.off()

    def stop_heating(self):
        self.is_working= False
        self._pin.on()