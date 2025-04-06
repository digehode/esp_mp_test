import network
import machine
from . import ping

STATUS_STRINGS = {
    network.STAT_IDLE: "no connection and no activity",
    network.STAT_CONNECTING: "connecting in progress",
    network.STAT_WRONG_PASSWORD: "failed due to incorrect password",
    network.STAT_NO_AP_FOUND: "failed because no access point replied",
    # network.STAT_CONNECT_FAIL: "failed due to other problems",
    network.STAT_GOT_IP: "connection successful",
    network.STAT_ASSOC_FAIL: "Association failed",
    network.STAT_BEACON_TIMEOUT: "Beacon timeout",
    network.STAT_HANDSHAKE_TIMEOUT: "Handshake timeout",
    network.STAT_NO_AP_FOUND_IN_AUTHMODE_THRESHOLD: "NO_AP_FOUND_IN_AUTHMODE_THRESHOLD",
    network.STAT_NO_AP_FOUND_IN_RSSI_THRESHOLD: "NO_AP_FOUND_IN_RSSI_THRESHOLD",
    network.STAT_NO_AP_FOUND_W_COMPATIBLE_SECURITY: "NO_AP_FOUND_W_COMPATIBLE_SECURITY",
}


class Wifi:
    def __init__(self, settings=None):
        self.wlan = network.WLAN(network.WLAN.IF_STA)
        self.ap_list = []
        self.settings = settings

    def status(self):
        return self.wlan.status()

    def status_string(self):
        return STATUS_STRINGS[self.status()]

    @property
    def connected(self):
        return self.wlan.isconnected()

    def wlan_available(self, ssid):
        ssid_b = ssid.encode("ASCII")
        print(f"Looking for {ssid_b}")
        for ap in self.ap_list:
            print(f"Comparing to {ap}")
            if ap[0] == ssid_b:
                return True
            return False

    def connect(self, ssid, password):
        hostname = "JS Platform"
        if self.settings is not None:
            if self.settings.HOSTNAME is not None:
                hostname = self.settings.HOSTNAME
        network.hostname(hostname)
        self.wlan.active(True)
        self.wlan.connect(ssid, password)
        while not self.wlan.isconnected():
            machine.idle()
        print("WLAN connection succeeded!")

    def scan(self):
        self.wlan.active(True)
        self.ap_list = self.wlan.scan()

    def info(self):
        data = {}
        ifc = self.wlan.ifconfig()
        data["ip"] = ifc[0]
        data["subnet"] = ifc[1]
        data["gateway"] = ifc[2]
        data["dns"] = ifc[3]
        data["mac"] = self.wlan.config("mac")
        data["ssid"] = self.wlan.config("ssid")
        data["hostname"] = network.hostname()
        return data


#  LocalWords:  Wifi ifconfig subnet dns
