from peripherals import Heater, TemperatureSensor
from time import sleep_ms

class VirtualTemperatureSensor(TemperatureSensor):
    def __init__(self,temperature,speed,heater : Heater,delay=250):
        self._speed:int = speed
        self._heater = heater
        self._delay = delay
        self._temperature = temperature

    def read_celsius(self) -> float:
        sign = 1 if self._heater.is_working else -1
        self._temperature = self._temperature + (self._speed * sign)
        sleep_ms(self._delay)
        return self._temperature