import network
import mqtt
from machine import Pin, I2C, ADC, UART, SPI, PWM
from time import sleep

#重启esp8266
# esp_vcc = Pin(24, Pin.OUT)
# esp_boot = Pin(21, Pin.OUT)
# esp_boot.value(0)
# esp_vcc.value(1)
# sleep(2)
# esp_vcc.value(0)

#连接wifi
N1 = network.WLAN_UART(network.STA_IF)
N1.active(True)
N1.connect("CHCK","depot0510")
sleep(1)
print('network information:', N1.ifconfig())
led = Pin(13, Pin.OUT)
button = Pin(12,Pin.IN)
led.value(1)

#配置mqtt
SERVER = 'mqtt.p2hp.com'
CLIENT_ID = 'esp8266_test'
TOPIC = 'webscket_test1'



#回调函数
def mqtt_callback(topic):
    print('topic: {}'.format(topic[0]))
    print('msg:{}'.format(topic[1]))
    
cl = mqtt.MQTTClient(CLIENT_ID, SERVER, mqtt_port = 1883)
#cl.set_callback(mqtt_callback)
cl.connect()
cl.set_callback(mqtt_callback)


#发布消息
#def MQTT_Send(tim)
#    client.publish(TOPIC, 'Hello Seeedstudio!')
cl.publish(TOPIC,"Hello Seeedstudio! Start")

#订阅“test”
#cl.subscribe(TOPIC)
#设置回调函数

#接收处理数据
while True:
    val = button.value()
    if(val == 1):
        cl.publish(TOPIC,"HIGH")
        break
    if(val == 0):
        cl.publish(TOPIC,"LOW")
        break
#    cl.wait_msg()
#   sleep(0.1)
