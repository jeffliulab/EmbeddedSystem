from lcd1602 import LCD1602  # 导入LCD库
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
d.print("Hello ")  # 第一行显示 "Hello"
sleep(1)           # 暂停1秒
d.setCursor(0, 1)  # 光标移动到第二行
d.print("world ")  # 第二行显示 "world"
