#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.

from network import WLAN
from mqtt import MQTTClient
import machine
import time

def settimeout(duration): 
    pass

wlan = WLAN(mode=WLAN.STA)
#wlan.antenna(WLAN.EXT_ANT)
wlan.connect("YOURSSID", auth=(WLAN.WPA2, "YOURPASSWORD"), timeout=30000)

while not wlan.isconnected(): 
     machine.idle()

print("Connected to Wifi\n")
client = MQTTClient(' ', 'test.mosquitto.org', port=1883, keepalive=30)
client.settimeout = settimeout
client.connect()

while True:
     print("Sending ON")
     client.publish(topic="/lights", msg="ON")
     time.sleep(5)
     print("Sending OFF")
     client.publish(topic="/lights", msg="OFF")
     time.sleep(5)
