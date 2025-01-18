class AppContext:
    def __init__(self, req_temp, up_heater, down_heater) -> None:
        self.required_temperature = req_temp
        self.up_heater_plugged = up_heater
        self.down_heater_plugged = down_heater