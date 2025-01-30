# If you haven't installed the picozero, you should firstly install picozero

from picozero import pico_temp_sensor
from time import sleep

while True:
    temperature = pico_temp_sensor.temp  # 读取温度
    print(f"Temperature: {temperature} °C")  # 打印温度
    sleep(1)  # 每隔1秒读取一次
