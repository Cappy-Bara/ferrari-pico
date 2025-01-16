from peripherals import Sensors, VirtualTemperatureSensor
from peripherals.Display.RealDisplay import RealDisplay
from peripherals.Heater.RealHeater import RealHeater
from peripherals.TemperatureSensor.RealTemperatureSensor import RealTemperatureSensor
from pin_inits import get_real_actuators, get_real_sensors
from pin_inits_mocks import get_mocked_actuators, get_mocked_sensors
from states import StateMachine, StateResult
from time import sleep_ms
import uasyncio as asyncio
from machine import Pin, I2C

# from webserver.server import GurgleAppsWebserver

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
        await asyncio.sleep(0.25)

def testHeater():
    h = RealHeater(5)
    h2 = RealHeater(6)
    while True:
        h.start_heating()
        h2.start_heating()
        sleep_ms(5000)
        h.stop_heating()
        h2.stop_heating()
        sleep_ms(500)

async def testTempSensor():
    h = RealTemperatureSensor(2,3,4)
    while True:
        val = await h.read_celsius()
        print("READING")
        print(val)
        sleep_ms(500)


sensor_i2c = I2C(1, scl=Pin(11), sda=Pin(10), freq=100000)
screen = RealDisplay(sensor_i2c,128,32)
s = StateResult(500, 137, False, False)

while(True):
    screen.display_state(s)
    sleep_ms(500)



# asyncio.run(testTempSensor())




# server = GurgleAppsWebserver(
#     port=80,
#     timeout=20,
#     doc_root="/www",
#     log_level=2
# )

# ssid = "UPC5980563"
# pw = "yM5j4Bdszneh"

# asyncio.run(server.start_server_with_background_task(main))
# print('DONE')

