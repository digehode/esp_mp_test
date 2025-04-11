from machine import Pin
from time import sleep

import js_platform
import mqtt_adapter


def main(settings):

    wifi = settings.wifi
    c = mqtt_adapter.MQTTAdapter(settings.HOSTNAME)
    c.initialise(
        settings.secrets["mqtt_server"],
        settings.secrets["mqtt_user"],
        settings.secrets["mqtt_password"],
    )
    c.add_action("debug", lambda: print("Got a debug message"))
    # c.publish(b"ESP", b"hello")
    # c.disconnect()

    while True:
        print("In the app, looping the loop")
        if wifi.connected:
            print(f"Connected to WIFI")
        else:
            print("Wifi not connected")
            print(f"Wifi status: {wifi.status_string()}")
        sleep(3)
        c.tick()


#  LocalWords:  uart baudrate rx
