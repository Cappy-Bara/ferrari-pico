from time import sleep
import machine

led = machine.Pin(5, machine.Pin.OUT)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)