from . import utils


def load_secrets(filename):
    secrets = {}
    if filename is not None:
        if not utils.exists(filename):
            raise Exception(f"Settings file ({filename}) not found")
        secrets = {}
        f = open(filename, "r")
        for l in f.readlines():
            k, v = l.split("=", 1)
            secrets[k.strip()] = eval(v.strip())
    return secrets
