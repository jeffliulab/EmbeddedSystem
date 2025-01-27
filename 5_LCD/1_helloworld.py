from lcd1602 import LCD1602  # 导入LCD库（need download into pico)
from machine import I2C, Pin  # 导入I2C和Pin模块
from utime import sleep      # 导入sleep函数

# 初始化I2C连接
i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)

# 初始化LCD
d = LCD1602(i2c, 2, 16)  # 2行16列LCD模块
d.display()              # 启用LCD显示

# 清空显示
d.clear()

# 显示文本
d.print("Hallo ")  # "hello" in the first line
sleep(1)           # stop 1s
d.setCursor(0, 1)  # cursor to second line
d.print("world ")  # "world" in the second line

sleep(1)
d.clear()