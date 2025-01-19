from device.peripherals.Heater.Plug import Plug

class AppContext:
    def __init__(self, req_temp, up_heater : bool, down_heater : bool) -> None:
        self.required_temperature = req_temp
        self.up_heater_plug = Plug(up_heater)
        self.down_heater_plug = Plug(down_heater)
        self.ip = ""