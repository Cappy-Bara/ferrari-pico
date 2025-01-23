from device.peripherals.Display.Display import Display
from device.states.StateMachine import StateResult
from libs.SSD1306.ssd1306 import SSD1306_I2C
from machine import I2C, Pin

class RealDisplay(Display):

    def __init__(self, scl, sda, width, height):
        display_i2c = I2C(0, scl = Pin(scl), sda = Pin(sda), freq=200000)
        self._display = SSD1306_I2C(width, height, display_i2c)
        self._ping = False

    def display_state(self, state : StateResult, ip : str):

        formatted_curr_temp = "{:.1f}".format(state.current_temperature)
        formatted_req_temp = "{:.1f}".format(state.required_temperature)

        top_working = "ON" if state.top_heater_state else "OFF"  
        bottom_working = "ON" if state.down_heater_state else "OFF"  

        self._display.text(f'T:{formatted_curr_temp}->{formatted_req_temp}',0,0)
        self._display.text(f'UP:{top_working}  DOWN:{bottom_working}',0,12)
        self._display.text(ip,0,24)

        if(self._ping):
            self._display.text('*',120,0)

        self._display.show()
        self._display.fill(0)
        self._ping = True if self._ping is False else False 
    
    def display_error(self):
        self._display.text(f'!!!!!!!!!!!!!!',0,0)
        self._display.text(f'!    ERROR   !',0,14)
        self._display.text(f'!!!!!!!!!!!!!!',0,28)
        self._display.show()
        self._display.fill(0)