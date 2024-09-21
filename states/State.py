from peripherals.Actuators import Actuators

class State():
    def handle(self, actuators : Actuators, current_temp: float, required_temp: float, hysteresis: float):
        raise NotImplementedError()