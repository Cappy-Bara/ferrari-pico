from peripherals.Actuators import Actuators
from peripherals.Sensors import Sensors
from states import State, HeatingState

class StateMachine:
    def __init__(self, sensors:Sensors, actuators:Actuators):
        self._sensors = sensors
        self._actuators = actuators

        self._current_state = HeatingState(self)

        self._was_temp_achieved= False

    async def handle(self, required_temp:float, hysteresis:float):
        current_temp = await self._sensors.temperature_reader.read_celsius()
        self._current_state.handle(self._actuators, current_temp, required_temp, hysteresis)
        return StateResult(current_temp, self._actuators.up_heater.is_working)
        
    def change_state(self, state:State):
        self._current_state= state

class StateResult:
    def __init__(self, current_temperature, top_heater_state) -> None:
        self.current_temperature = current_temperature
        self.top_heater_state = top_heater_state