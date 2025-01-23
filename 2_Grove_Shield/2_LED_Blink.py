import machine
from machine import Pin
from utime import sleep
from machine import Timer

pin = Pin("LED", Pin.OUT)
LED = machine.Pin(16, machine.Pin.OUT)


print("LED starts flashing...")
def blink(timer):
    pin.toggle()
    LED.toggle()

tim = Timer()

tim.init(freq=2, mode=Timer.PERIODIC, callback=lambda t:blink(t))


