from peripherals.Actuators import Actuators
from states import State

class SustainState(State):

    def __init__(self, state_machine, was_heated : bool):
        self._state_machine = state_machine
        self._was_heated = was_heated

    def handle(self, actuators : Actuators, current_temp: float, required_temp: float, hysteresis: float):
        from states import HeatingState
        actuators.up_heater.stop_heating()

        if(current_temp < required_temp - hysteresis):
            self._state_machine.change_state(HeatingState(self._state_machine))