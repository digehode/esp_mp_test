from machine import Pin
from time import sleep

import js_platform


ssid = "Unbelievable Krimewave"
password = "ba55OON-|-|-<"


def main():
    led = Pin(8, Pin.OUT)

    wifi = js_platform.wifi.Wifi()
    wifi.connect(ssid, password)

    while True:
        print("In the app, looping the loop")
        if wifi.connected:
            print(f"Connected to WIFI")
        else:
            print("Wifi not connected")
            print(f"Wifi status: {wifi.status_string()}")
        led.value(1)
        sleep(1)
        led.value(0)
        sleep(1)


#  LocalWords:  uart baudrate rx
