from peripherals.Actuators import Actuators
from states import State

class HeatingState(State):
    def __init__(self, state_machine):
        self._state_machine = state_machine

    def handle(self, actuators : Actuators, current_temp: float, required_temp: float, hysteresis: float):
        from states import SustainState
        actuators.up_heater.start_heating()

        if(current_temp >= required_temp):
            self._state_machine.change_state(SustainState(self._state_machine, True))