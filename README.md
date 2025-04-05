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

```python
import js_platform

# App to load and run
APP = "blink_app"

# File containing vars not to be checked in to repo
# Set to None if not required
SECRETS_FILE = "./secrets.txt"

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
