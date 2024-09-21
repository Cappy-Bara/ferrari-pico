from peripherals import TemperatureSensor

class Sensors:
    def __init__(self, temperature_sensor:TemperatureSensor):
        self.temperature_reader = temperature_sensor