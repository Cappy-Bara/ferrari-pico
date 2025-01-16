from device.peripherals.Heater.Heater import Heater

class Actuators:
    def __init__(self, up_heater : Heater, down_heater : Heater):
        self.up_heater = up_heater
        self.down_heater = down_heater