import json


def load():
    """
    This functions loads all JSON file.
    """
    # for key, value in settings.items():
    # settings[key] = value

    # accounts = json.load(open("data/accounts.json", "r"))
    addresses = json.load(open("data/addresses.json", "r"))
    # classes = json.load(open("data/classes.json", "r"))
    corrections = json.load(open("data/corrections.json", "r"))
    donations_in_kind = json.load(open("data/donations_in_kind.json", "r"))
    # groups = json.load(open("data/groups.json", "r"))
    mappings = json.load(open("data/mappings.json", "r"))
    settings = json.load(open("data/settings.json", "r"))
    templates = json.load(open("data/templates.json", "r"))

    return addresses, corrections, donations_in_kind, mappings, settings, templates
