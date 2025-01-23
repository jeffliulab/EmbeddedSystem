from machine import Pin
from utime import sleep
from machine import Timer

pin = Pin("LED", Pin.OUT)

print("LED starts flashing...")
def blink(timer):
    pin.toggle()

tim = Timer()

tim.init(freq=10, mode=Timer.PERIODIC, callback=lambda t:blink(t))






# freq=10 表示每秒执行10次（开-关各5次，实现5次完整闪烁）
# mode=Timer.PERIODIC 设置为周期性模式，这样会持续闪烁




"""

==================DEF TIMER

from machine import Pin
from utime import sleep
from machine import Timer

def blink(timer):
    # led toggle

timer = Timer()
timer.init(freq=10, mode=Timer.PERIODIC, callback=blink)
tim = Timer(period=5000, mode=Timer.ONE_SHOT, callback=lambda t:print(1))

"""