from device.states.StateMachine import StateResult

class Display():
    def display_state(self, result: StateResult):
        raise NotImplementedError

    def display_error(self):
        raise NotImplementedError