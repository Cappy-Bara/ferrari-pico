from device.peripherals.Actuators import Actuators
from device.states.State import State

class HeatingState(State):
    def __init__(self, state_machine):
        self._state_machine = state_machine

    def handle(self, actuators : Actuators, current_temp: float, required_temp: float, hysteresis: float):
        actuators.up_heater.start_heating()
        actuators.down_heater.start_heating()

        from device.states.SustainState import SustainState

        if(current_temp >= required_temp):
            self._state_machine.change_state(SustainState(self._state_machine, True))