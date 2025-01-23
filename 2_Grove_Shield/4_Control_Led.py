"""
Grove - Rotary Angle Sensor
Grove - Rotary Angle Sensor can change the resistance
value to achieve different output levels by rotating the
300-degree adjusting knob on the potentiometer. It has a
maximum resistance value of 10KΩ.
"""

# 导入必要的库
from machine import Pin, ADC, PWM

# 初始化旋转角度传感器和LED
ROTARY_ANGLE_SENSOR = ADC(0)  # 旋转角度传感器连接到A0
LED_PWM = PWM(Pin(16))        # LED连接到D18

# 设置PWM频率
LED_PWM.freq(500)

while True:
    # 读取旋转角度传感器的值
    val = ROTARY_ANGLE_SENSOR.read_u16()
    # 将读取值作为PWM占空比
    LED_PWM.duty_u16(val)
