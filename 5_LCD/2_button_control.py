from lcd1602 import LCD1602  # LCD lib - need download into pico)
from machine import I2C, Pin  # I2C and Pin module
from utime import sleep      # sleep function

# initialzie I2C
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)

# initialize LCD
d = LCD1602(i2c, 2, 16)  # 2行16列LCD模块
d.display()              # 启用LCD显示

# clear LCD
d.clear()

# print in LCD
d.print("Hallo ")  # "hello" in the first line
sleep(1)           # stop 1s
d.setCursor(0, 1)  # cursor to second line
d.print("world ")  # "world" in the second line

sleep(1)
d.clear()

############ USE BUTTON TO CONTROL ####################

# initialize button
b = Pin(18, Pin.IN, Pin.PULL_UP) ## Button: D18

while True:                          # 主循环, 读取按钮状态，当b.value()的时候，属于button被按下的状态，因为上面是PULL_UP？
    if not b.value():  
        d.clear()
        d.print("Hello World!")
        sleep(0.5)                                           # 防抖延时
    else:
        d.clear()
    
    sleep(0.1)                                               # 循环延时，防止CPU占用过高