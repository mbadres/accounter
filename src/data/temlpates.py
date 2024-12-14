from data.settings import placeholder

_descriptions = {
    "donation": f"Spende von {placeholder}",
    "purchase": f"Erwerb von {placeholder}",
    "discount": f"Abschlag für {placeholder}",
    "provision": f"Bereitstellung von {placeholder}",
    "insurance": f"Versicherung von {placeholder}",
    "refund": f"Erstattung von {placeholder}",
    "pastoral ministry": "Pfarrdienst",
    "transfer": "Umbuchung",
}

templates = {
    "general_donation": {
        "description": f"Spende von {placeholder}",
        "debit_account": 1000,
        "credit_account": 3100,
    },
    "church_construction_donation": {
        "description": f"Spende von {placeholder}",
        "debit_account": 1010,
        "credit_account": 3100,
    },
    "congregation_materials": {
        "description": f"Spende von {placeholder}",
        "debit_account": 4200,
        "credit_account": 1010,
    },
}
