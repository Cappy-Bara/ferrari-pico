from peripherals.TemperatureSensor.TemperatureSensor import TemperatureSensor
from asyncio import sleep

class MockedTemperatureSensor(TemperatureSensor):
    def __init__(self, delay=0.250):
        self._required_ticks:int = 0
        self._count:int = 1
        self._mocked_temperature:float = 0
        self._gradient:float = 0
        self._delay = delay

    async def read_celsius(self) -> float:

        if(self._count < self._required_ticks):
            self._count = self._count+1
            await sleep(self._delay)
            self._mocked_temperature=self._mocked_temperature + self._gradient
            return self._mocked_temperature

        self._mocked_temperature = float(input('MOCKED TEMPERATURE: '))
        self._required_ticks = int(input('NUMBER OF TICKS: '))
        self._gradient = int(input('GRADIENT: '))
        self._count = 1

        await sleep(self._delay)

        return self._mocked_temperature