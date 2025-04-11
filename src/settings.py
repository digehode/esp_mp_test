import js_platform

# App to load and run
APP = "neo_pixel_demo"

# File containing vars not to be checked in to repo
# Set to None if not required
SECRETS_FILE = "./secrets.txt"


# File containing micropython library requirements, one per line
# Set to None if not required
REQUIREMENTS_FILE = "./mp_requirements.txt"


# Set to True in order to connect to wifi on boot settings.wifi will
# be the wlan object resulting, or None if WIFI_ON_BOOT is set to
# False.
# Needed if you have to install packages.

WIFI_ON_BOOT = True

# The hostname used for connecting to the network
HOSTNAME = "esp-test"


# --- No need to edit below

# Import the app
app = __import__(APP)

# Load secrets
secrets = js_platform.settings.load_secrets(SECRETS_FILE)
