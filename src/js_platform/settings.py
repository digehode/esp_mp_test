from . import utils


def install_requirements(filename):
    import mip

    if filename is not None:
        if not utils.exists(filename):
            raise Exception(f"Requirements file ({filename}) not found")
        f = open(filename, "r")
        for l in f.readlines():
            mip.install(l.strip())


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


#  LocalWords:  mip
