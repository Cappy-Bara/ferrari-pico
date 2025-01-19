
from device.peripherals.Actuators import Actuators
from device.peripherals.Display.RealDisplay import RealDisplay
from device.peripherals.Heater.Plug import Plug
from device.peripherals.Heater.RealHeater import RealHeater
from device.peripherals.Sensors import Sensors
from device.peripherals.TemperatureSensor.RealTemperatureSensor import RealTemperatureSensor

def get_real_sensors() -> Sensors:
    temperatureSensor = RealTemperatureSensor(2,3,4)
    return Sensors(temperatureSensor)

def get_real_actuators(upPlug : Plug, downPlug : Plug) -> Actuators:
    up_heater = RealHeater(5,upPlug)
    down_heater = RealHeater(6, downPlug)
    return Actuators(up_heater, down_heater)

def get_real_display():
    display = None
    try:
        scl = 17
        sda = 16
        display = RealDisplay(scl, sda, 128, 64)
    except:
        print("Display cannot be initialized.")
    
    return display