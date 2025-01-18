from AppContext import AppContext
from device.peripherals.TemperatureSensor.VirtualTemperatureSensor import VirtualTemperatureSensor
from device.peripherals.pin_inits_mocks import get_mocked_actuators, get_mocked_sensors
from device.states.StateMachine import StateMachine, StateResult
from device.peripherals.pin_inits import get_real_actuators, get_real_sensors
import json
import uasyncio as asyncio

context : AppContext = None  # type: ignore
currentState: StateResult = None # type: ignore

async def handle_device(appContext:AppContext, beginState : StateResult):
    global context, currentState
    context = appContext
    currentState = beginState

    # actuators = get_real_actuators()
    # sensors = get_real_sensors()

    actuators = get_mocked_actuators()
    sensors = get_mocked_sensors()
    sensors.temperature_reader = VirtualTemperatureSensor(50,1,actuators.up_heater)

    HYSTERESIS = 20

    stateMachine = StateMachine(sensors, actuators)

    while True:
        result = await stateMachine.handle(context.required_temperature, HYSTERESIS)
        currentState.update(result) 

        await asyncio.sleep(0.25)