from max6675.max6675 import MAX6675
from machine import Pin
import time

sck = Pin(2, Pin.OUT)
cs = Pin(3, Pin.OUT)
so = Pin(4, Pin.IN)

sensor = MAX6675(sck, cs , so)

while True:
    print("temperature=")
    print(sensor.read())
    time.sleep(1)