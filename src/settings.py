import js_platform

# App to load and run
APP = "blink_app"

# File containing vars not to be checked in to repo
# Set to None if not required
SECRETS_FILE = "./secrets.txt"

app = __import__(APP)


# Load secrets
secrets = js_platform.settings.load_secrets(SECRETS_FILE)
