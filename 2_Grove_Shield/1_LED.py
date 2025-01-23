import machine
LED = machine.Pin(16, machine.Pin.OUT)

# value(1) means the light on
LED.value(1)

# value(0) means the light off
LED.value(0)