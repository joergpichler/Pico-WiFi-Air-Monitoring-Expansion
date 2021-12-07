from ssd1306 import SSD1306_I2C
from machine import I2C, Pin

#from machine import UART, Pin
import time

#u = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1), bits=8, parity=None, stop=1)
#startBit = False
#while True:
#    b = u.read(1)
#    if b == b'\x42':
#        startBit = True
#        print('yeah')
#    elif startBit and b == b'\x4d':
#        print('yeah yeah')
#    else:
#        startBit = False
        
#    time.sleep(0.1)
WIDTH  = 128                                            # oled display width
HEIGHT = 32                                             # oled display height

i2c = I2C(0, freq=399361, scl=Pin(21), sda=Pin(20))

oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display

oled.fill(0)

i = 0
j = 0
k = 0
while True:
    oled.fill(0)
    oled.text("Counter: {}".format(i),5,5)
    oled.text("Counter: {}".format(j),5,15)
    oled.text("Counter: {}".format(k),5,25)
    oled.show()
    i += 1
    j += 2
    k += 3
    time.sleep(1)

    
