# ---- Let LED on RaspberryPi blink -----

import machine
import time

def let_blink(duration = 5):
    led = machine.Pin('LED', machine.Pin.OUT)

    while(duration > 0):
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)
        duration -= 1
        print('blink')
    
    print('Done blinking ;)')
    