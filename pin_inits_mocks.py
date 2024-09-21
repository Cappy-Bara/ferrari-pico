from peripherals import Actuators, Sensors, MockedHeater, MockedTemperatureSensor

def get_mocked_sensors() -> Sensors:
    temperatureSensor = MockedTemperatureSensor()
    return Sensors(temperatureSensor)

def get_mocked_actuators() -> Actuators:
    up_heater = MockedHeater("UP") 
    return Actuators(up_heater)