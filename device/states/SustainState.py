from device.peripherals.Actuators import Actuators
from device.states.State import State

class SustainState(State):

    def __init__(self, state_machine, was_heated : bool):
        self._state_machine = state_machine
        self._was_heated = was_heated

    def handle(self, actuators : Actuators, current_temp: float, required_temp: float, hysteresis: float):
        actuators.up_heater.stop_heating()

        from device.states.HeatingState import HeatingState

        if(current_temp < required_temp - hysteresis):
            self._state_machine.change_state(HeatingState(self._state_machine))