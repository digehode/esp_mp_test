from machine import Pin
from time import sleep
from simple import MQTTClient

import js_platform


def main(settings):

    wifi = settings.wifi
    c = MQTTClient(
        settings.HOSTNAME,
        settings.secrets["mqtt_server"],
        user=settings.secrets["mqtt_user"],
        password=settings.secrets["mqtt_password"],
    )
    c.connect(timeout=10)
    c.publish(b"ESP", b"hello")
    c.disconnect()

    while True:
        print("In the app, looping the loop")
        if wifi.connected:
            print(f"Connected to WIFI")
        else:
            print("Wifi not connected")
            print(f"Wifi status: {wifi.status_string()}")
        sleep(3)


#  LocalWords:  uart baudrate rx
