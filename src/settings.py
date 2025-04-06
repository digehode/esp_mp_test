import js_platform

# App to load and run
APP = "umqtt_test"

# File containing vars not to be checked in to repo
# Set to None if not required
SECRETS_FILE = "./secrets.txt"


# File containing micropython library requirements, one per line
# Set to None if not required
REQUIREMENTS_FILE = "./mp_requirements.txt"


# The hostname used for connecting to the network
HOSTNAME = "esp-test"


# --- No need to edit below

# Import the app
app = __import__(APP)

# Load secrets
secrets = js_platform.settings.load_secrets(SECRETS_FILE)
