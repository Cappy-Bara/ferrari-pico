from libs.max6675.max6675 import MAX6675
from machine import Pin
from peripherals.TemperatureSensor.TemperatureSensor import TemperatureSensor 

class RealTemperatureSensor(TemperatureSensor):
    def __init__(self, sckPinNumber:int, csPinNumber:int, soPinNumber:int):
        sck = Pin(sckPinNumber, Pin.OUT)
        cs = Pin(csPinNumber, Pin.OUT)
        so = Pin(soPinNumber, Pin.IN)

        self.sensor = MAX6675(sck, cs, so)

    async def read_celsius(self) -> float:
        return await self.sensor.read()