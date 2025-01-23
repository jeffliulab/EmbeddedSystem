import machine
from machine import Pin, PWM
from utime import sleep

# 初始化 LED 的 PWM
pwm_led = PWM(Pin(16))  # 使用 GPIO16
pwm_led.freq(1000)      # 设置 PWM 频率为 1000 Hz

# 定义占空比
brightness = 0          # 初始化亮度为 0
fade_direction = 1      # 亮度变化方向（1 为增加，-1 为减少）

# 开始 LED 的亮度变化
print("LED starts fading with PWM...")
while True:
    pwm_led.duty_u16(brightness)  # 设置占空比（16 位）
    brightness += fade_direction * 500  # 调节亮度
    if brightness >= 65535 or brightness <= 0:
        fade_direction *= -1  # 反转方向
    sleep(0.01)  # 控制变化速度
