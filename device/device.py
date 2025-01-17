from AppContext import AppContext
from device.states.StateMachine import StateMachine
from .peripherals.pin_inits import get_real_actuators, get_real_sensors
import uasyncio as asyncio

context : AppContext = None  # type: ignore

async def handle_device(appContext:AppContext):
    global context
    context = appContext

    actuators = get_real_actuators()
    sensors = get_real_sensors()

    REQUIRED_TEMPERATURE = 500
    HYSTERESIS = 20

    stateMachine = StateMachine(sensors, actuators)

    # sensor_i2c = I2C(1, scl=Pin(11), sda=Pin(10), freq=100000)
    # screen = RealDisplay(sensor_i2c,128,32)
    # s = StateResult(500, 137, False, False)

    while True:
        print(f"UP => {context.up_heater_plugged}")
        print(f"DOWN => {context.down_heater_plugged}")
        print(f"Temp => {context.required_temperature}")
        #stateResult = await stateMachine.handle(REQUIRED_TEMPERATURE, HYSTERESIS)
        await asyncio.sleep(0.25)