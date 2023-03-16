# ---- Connect to WIFI by SSID and PW -----
# Returns the id of the RaspberryPi Pico in the WIFI

import network
import time
from secrets import secrets

def connect_to_wifi(ssid = secrets['ssid'], psk = secrets['password']):
     # ---- Detecting nearby WIFI networks -----
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, psk)
 
    # Wait for connect or fail
    wait = 10
    while wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        wait -= 1
        print('waiting for connection...')
        time.sleep(1)
 
    # Handle connection error
    if wlan.status() != 3:
        raise RuntimeError('wifi connection failed')
    else:
        if wlan.isconnected():
            print("Connected to", ssid)
            
        ip = wlan.ifconfig()[0]
        print('network config: ', ip)
        return ip
