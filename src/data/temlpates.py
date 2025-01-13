from data.settings import placeholder, no_template

_descriptions = {
    "donation": f"Spende von {placeholder}",
    "purchase": f"Erwerb von {placeholder}",
    "payment": f"Zahlung an {placeholder}",
    "discount": f"Abschlag für {placeholder}",
    "provision": f"Bereitstellung von {placeholder}",
    "insurance": f"Versicherung von {placeholder}",
    "refund": f"Erstattung von {placeholder}",
    "pastoral ministry": "Pfarrdienst",
    "transfer": "Umbuchung",
}

templates = {
    "account_management_charge": {
        "description": f"Gebühr für die Kontoführung",
        "debit_account": 5500,
        "credit_account": 1100,
    },
    "broadcasting_fee": {
        "description": f"Rundfunkbeitrag",
        "debit_account": 0,
        "credit_account": 1100,
    },
    "cash_to_bank": {
        "description": f"FEHLER",
        "debit_account": 0,
        "credit_account": 0,
    },
    "church_construction_donation": {
        "description": f"Spende von {placeholder}",
        "debit_account": 1110,
        "credit_account": 3100,
    },
    "congregation_materials": {
        "description": f"Spende von {placeholder}",
        "debit_account": 4200,
        "credit_account": 1100,
    },
    "general_donation": {
        "description": f"Spende von {placeholder}",
        "debit_account": 1100,
        "credit_account": 3100,
    },
    "insurance": {
        "description": f"FEHLER",
        "debit_account": 0,
        "credit_account": 1100,
    },
    "interest_income": {
        "description": f"FEHLER",
        "debit_account": 1120,
        "credit_account": 5100,
    },
    "internet_bill": {
        "description": f"FEHLER",
        "debit_account": 0,
        "credit_account": 1100,
    },
    "pastoral_ministry": {
        "description": f"Zahlung für den Pfarrdienst",
        "debit_account": 4100,
        "credit_account": 1100,
    },
    "support_diocese": {
        "description": f"Unterstützung für das Bistum",
        "debit_account": 4300,
        "credit_account": 1100,
    },
    "von_kirchbau_nach_laufend": {
        "description": f"FEHLER",
        "debit_account": 0,
        "credit_account": 0,
    },
    "von_laufen_nach_spar": {
        "description": f"FEHLER",
        "debit_account": 0,
        "credit_account": 0,
    },
    "water_consumption": {
        "description": f"FEHLER",
        "debit_account": 0,
        "credit_account": 1100,
    },
    no_template: {
        "description": f"FEHLER",
        "debit_account": 0,
        "credit_account": 0,
    },
}
