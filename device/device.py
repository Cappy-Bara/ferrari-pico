from AppContext import AppContext
from device.peripherals.Display.RealDisplay import RealDisplay
from device.peripherals.TemperatureSensor.VirtualTemperatureSensor import VirtualTemperatureSensor
from device.peripherals.pin_inits_mocks import get_mocked_actuators, get_mocked_sensors
from device.states.StateMachine import StateMachine, StateResult
from device.peripherals.pin_inits import get_real_actuators, get_real_display, get_real_sensors
import uasyncio as asyncio

context : AppContext = None  # type: ignore
currentState: StateResult = None # type: ignore

async def handle_device(appContext:AppContext, beginState : StateResult):
    global context, currentState
    context = appContext
    currentState = beginState

    display = get_real_display()
    actuators = get_real_actuators(appContext.up_heater_plug, appContext.down_heater_plug)
    sensors = get_real_sensors()

    HYSTERESIS = 20

    stateMachine = StateMachine(sensors, actuators)

    while True:
        result = await stateMachine.handle(context.required_temperature, HYSTERESIS)
        currentState.update(result)

        if(display is not None):
            try:
                display.display_state(currentState,appContext.ip)
            except:
                print("Error while printing data on screen.")

        await asyncio.sleep(0.25)