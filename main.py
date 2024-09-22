from peripherals import Sensors, VirtualTemperatureSensor
from pin_inits import get_real_actuators, get_real_sensors
from pin_inits_mocks import get_mocked_actuators, get_mocked_sensors
from states import StateMachine
from time import sleep_ms
import asyncio

##init
actuators = get_real_actuators()
temperature_sensor = VirtualTemperatureSensor(400, 5, actuators.up_heater)
sensors = Sensors(temperature_sensor)

REQUIRED_TEMPERATURE = 500
HYSTERESIS = 20

stateMachine = StateMachine(sensors, actuators)

async def main():
    while True:
        stateResult = await stateMachine.handle(REQUIRED_TEMPERATURE, HYSTERESIS)
        print(f"CURRENT TEMPERATURE:{stateResult.current_temperature}")
        print(f"HEATER STATE:{stateResult.top_heater_state}")
        await asyncio.sleep(0.25)

asyncio.run(main())