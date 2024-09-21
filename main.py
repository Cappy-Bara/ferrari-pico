from peripherals import Sensors, VirtualTemperatureSensor
from pin_inits import get_real_actuators
from pin_inits_mocks import get_mocked_actuators, get_mocked_sensors
from states import StateMachine
from time import sleep_ms

##init
actuators = get_real_actuators()
temperature_sensor = VirtualTemperatureSensor(400, 5, actuators.up_heater)
sensors = Sensors(temperature_sensor)

REQUIRED_TEMPERATURE = 500
HYSTERESIS = 20

stateMachine = StateMachine(sensors, actuators)

def handle():
    stateResult = stateMachine.handle(REQUIRED_TEMPERATURE, HYSTERESIS)
    print(f"CURRENT TEMPERATURE:{stateResult.current_temperature}")
    print(f"HEATER STATE:{stateResult.top_heater_state}")
    return

while True:
    handle()
    sleep_ms(1)