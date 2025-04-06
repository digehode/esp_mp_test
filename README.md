# Testing ESP32 development with micropython


## Flashing
`esptool.py erase_flash`
`esptool.py --baud 460800 write_flash 0 [binary]`



# Platform

## `boot.py`

Initialises the board.

JSPlatform includes the following additional funcitonality:

 - `soft_reset()` defined in `boot.py` so that a simple `soft_reset()`
   at the REPL prompt can be used to reset and load new code.
   
## `main.py` 

Runs applicaiton code.

Import whatever app as `app`. The package should have a function
called `main()` that will be used to begin app execution.

## `settings.py`

App settings file.

Currently requires only `APP` to be set, but can also load secrets so
that passwords, keys, etc don't have to be stored in source and can be
easily kept out of repos.

`REQUIREMENTS_FILE` is a filename or None. If it is a file, a list of
sources (in any format
[mip](https://docs.micropython.org/en/latest/reference/packages.html#installing-packages-with-mip)
accepts), one per line, should be in it. These will be installed on
launch.  It will get re-processed on even a soft reset, but mip knows
when something already exists so will cause no issues other than the
slight overhead.

```python
import js_platform

# App to load and run
APP = "blink_app"

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
```

# To Do

## Config/settings
 - Add optional settings file
  - Set ip application config items 
  - Define which app is loaded
  - Add additional boot operations 
