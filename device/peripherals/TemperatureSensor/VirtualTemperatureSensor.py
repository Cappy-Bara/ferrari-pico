from asyncio import sleep
from device.peripherals.Heater.Heater import Heater
from device.peripherals.TemperatureSensor.TemperatureSensor import TemperatureSensor

class VirtualTemperatureSensor(TemperatureSensor):
    def __init__(self,temperature,speed,heater : Heater,delay=0.250):
        self._speed:int = speed
        self._heater = heater
        self._delay = delay
        self._temperature = temperature

    async def read_celsius(self) -> float:
        sign = 1 if self._heater.is_working else -1
        self._temperature = self._temperature + (self._speed * sign)
        await sleep(self._delay)
        return self._temperature