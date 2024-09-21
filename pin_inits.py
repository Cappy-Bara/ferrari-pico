from peripherals import Actuators, Sensors, RealHeater, RealTemperatureSensor

def get_real_sensors() -> Sensors:
    temperatureSensor = RealTemperatureSensor(2,3,4)
    return Sensors(temperatureSensor)

def get_real_actuators() -> Actuators:
    up_heater = RealHeater(5)
    return Actuators(up_heater)