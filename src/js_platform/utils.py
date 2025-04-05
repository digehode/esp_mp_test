import os


def exists(filename):
    try:
        os.stat(filename)
        return True
    except OSError:
        return False
