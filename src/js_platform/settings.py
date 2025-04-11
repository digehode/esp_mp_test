from . import utils


def install_requirements(filename):
    import mip

    if filename is not None:
        if not utils.exists(filename):
            raise Exception(f"Requirements file ({filename}) not found")
        with open(filename, "r") as f:
            for line in f.readlines():
                line = line.strip()
                if not line.startswith("#"):
                    mip.install(line)


def load_secrets(filename):
    secrets = {}
    if filename is not None:
        if not utils.exists(filename):
            raise Exception(f"Settings file ({filename}) not found")
        secrets = {}
        f = open(filename, "r")
        for line in f.readlines():
            line = line.strip()
            if line.startswith("#"):
                continue
            k, v = line.split("=", 1)
            secrets[k.strip()] = eval(v.strip())
    return secrets


#  LocalWords:  mip
