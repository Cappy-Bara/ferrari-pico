
from device.peripherals.Actuators import Actuators
from device.peripherals.Heater.RealHeater import RealHeater
from device.peripherals.Sensors import Sensors
from device.peripherals.TemperatureSensor.RealTemperatureSensor import RealTemperatureSensor


def get_real_sensors() -> Sensors:
    temperatureSensor = RealTemperatureSensor(2,3,4)
    return Sensors(temperatureSensor)

def get_real_actuators() -> Actuators:
    up_heater = RealHeater(5)
    down_heater = RealHeater(6)
    return Actuators(up_heater, down_heater)