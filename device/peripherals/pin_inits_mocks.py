
from device.peripherals.Actuators import Actuators
from device.peripherals.Heater.MockedHeater import MockedHeater
from device.peripherals.Heater.Plug import Plug
from device.peripherals.Sensors import Sensors
from device.peripherals.TemperatureSensor.MockedTemperatureSensor import MockedTemperatureSensor


def get_mocked_sensors() -> Sensors:
    temperatureSensor = MockedTemperatureSensor()
    return Sensors(temperatureSensor)

def get_mocked_actuators(upPlug : Plug, downPlug : Plug) -> Actuators:
    up_heater = MockedHeater("UP",upPlug) 
    down_heater = MockedHeater("DOWN", downPlug) 
    return Actuators(up_heater,down_heater)