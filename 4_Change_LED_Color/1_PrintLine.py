from machine import ADC, Pin
import neopixel
import utime

led_pin = Pin(20, Pin.OUT) 
num_leds = 1                                        # WS2813 Mini 只有一个 LED
np = neopixel.NeoPixel(led_pin, num_leds)

# **旋钮（电位器）连接在 A0 (对应 GP26, ADC0)**
pot = ADC(26)

def map_value(value, in_min, in_max, out_min, out_max):
    """ 线性映射函数：将 value 从 in_min-in_max 映射到 out_min-out_max """
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def set_color(r, g, b):
    """ 设置 WS2813 RGB LED 颜色 """
    np[0] = (r, g, b)
    np.write()

# **记录开始时间**
start_time = utime.time()

while True:
    current_time = utime.time()  # 获取当前时间
    if current_time - start_time >= 60:  # **如果运行时间超过 60 秒，就跳出循环**
        print("循环结束，程序停止")
        break  # **终止 while 循环**

    pot_value = pot.read_u16()  # 读取旋钮值 (0 - 65535)

    # **映射颜色**
    red = map_value(pot_value, 0, 65535, 0, 255)
    green = map_value(65535 - pot_value, 0, 65535, 0, 255)
    blue = map_value(pot_value % 32768, 0, 32767, 0, 255)

    # **应用颜色**
    set_color(red, green, blue)

    print(f"旋钮值: {pot_value}, R:{red}, G:{green}, B:{blue}")
    utime.sleep(0.05)  # **短延迟，避免刷新过快**
