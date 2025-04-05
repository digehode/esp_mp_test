import machine
import sys
import settings


try:
    print(f"Beginning application: {settings.app.__name__}")
    settings.app.main(settings)
except Exception as e:
    print("Fatal error in main:")
    print(e)
    sys.print_exception(e)

# Following a normal Exception or main() exiting, reset the board.
# Following a non-Exception error such as KeyboardInterrupt (Ctrl-C),
# this code will drop to a REPL. Place machine.reset() in a finally
# block to always reset, instead.

# machine.reset()
