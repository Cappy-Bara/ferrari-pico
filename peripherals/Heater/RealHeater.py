from peripherals.Heater.Heater import Heater
import machine

class RealHeater(Heater):

    def __init__(self, heaterPin:int):
        self.is_working = False
        self._pin = machine.Pin(heaterPin, machine.Pin.OUT)

    def start_heating(self):
        self.is_working = True
        self._pin.on()

    def stop_heating(self):
        self.is_working= False
        self._pin.off()