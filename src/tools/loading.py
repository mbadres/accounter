import json


def load(path):
    """
    This functions loads the settings from a JSON file.
    """
    settings = json.load(open(path, "r"))
    print(settings)
    # for key, value in settings.items():
    # settings[key] = value
