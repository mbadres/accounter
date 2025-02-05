from models.account import Account
from models.account_type import AccountType

accounts = {
    0: Account(
        number=0,
        description="FEHLER",
        type=AccountType.ASSET_ACCOUNT,
    ),
    200: Account(
        number=200,
        description="Unbebaute Grundstücke",
        type=AccountType.ASSET_ACCOUNT,
    ),
    210: Account(
        number=210,
        description="Bebaute Grundstücke",
        type=AccountType.ASSET_ACCOUNT,
    ),
    250: Account(
        number=250,
        description="Kirchengebäude",
        type=AccountType.ASSET_ACCOUNT,
    ),
    255: Account(
        number=255,
        description="Sonstige Gebäude",
        type=AccountType.ASSET_ACCOUNT,
    ),
    400: Account(
        number=400,
        description="Liturgische Ausstattung",
        type=AccountType.ASSET_ACCOUNT,
    ),
    410: Account(
        number=410,
        description="Büroausstattung",
        type=AccountType.ASSET_ACCOUNT,
    ),
    420: Account(
        number=420,
        description="IT-Ausstattung",
        type=AccountType.ASSET_ACCOUNT,
    ),
    1000: Account(
        number=1000,
        description="Kasse",
        type=AccountType.ASSET_ACCOUNT,
    ),
    1100: Account(
        number=1100,
        description="Konto für Laufendes",
        type=AccountType.ASSET_ACCOUNT,
    ),
    1110: Account(
        number=1110,
        description="Kirchbaukonto",
        type=AccountType.ASSET_ACCOUNT,
    ),
    1120: Account(
        number=1120,
        description="Sparkonto",
        type=AccountType.ASSET_ACCOUNT,
    ),
    2200: Account(
        number=2200,
        description="Freie Rücklagen",
        type=AccountType.LIABILITY_ACCOUNT,
    ),
    2210: Account(
        number=2210,
        description="Betriebsmittelrücklage",
        type=AccountType.LIABILITY_ACCOUNT,
    ),
    2220: Account(
        number=2220,
        description="Rücklagen für Bau und Instandhaltung",
        type=AccountType.LIABILITY_ACCOUNT,
    ),
    2300: Account(
        number=2300,
        description="Steuerrückstellungen",
        type=AccountType.LIABILITY_ACCOUNT,
    ),
    2310: Account(
        number=2310,
        description="Sonstige Rückstellungen",
        type=AccountType.LIABILITY_ACCOUNT,
    ),
    3100: Account(
        number=3100,
        description="Allgemeine Spenden",
        type=AccountType.REVENUE_ACCOUNT,
    ),
    3110: Account(
        number=3110,
        description="Zweckgebundene Spenden",
        type=AccountType.REVENUE_ACCOUNT,
    ),
    3120: Account(
        number=3120,
        description="Kollekte",
        type=AccountType.REVENUE_ACCOUNT,
    ),
    3200: Account(
        number=3200,
        description="Öffentliche Zuschüsse",
        type=AccountType.REVENUE_ACCOUNT,
    ),
    3210: Account(
        number=3210,
        description="Kirchliche Zuschüsse",
        type=AccountType.REVENUE_ACCOUNT,
    ),
    3501: Account(
        number=3501,
        description="Pfarrdienst",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3502: Account(
        number=3502,
        description="Materialien für den Gottesdienst",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3503: Account(
        number=3503,
        description="Materialien für die Sonntagschule oder ähnliches",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3504: Account(
        number=3504,
        description="Bezuschussung von Treffen, Ausflügen und anderen Unternehmungen",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3505: Account(
        number=3505,
        description="Gemeinschaftsessen",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3506: Account(
        number=3506,
        description="Fahrtkostenerstattung für Seelsorge",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3507: Account(
        number=3507,
        description="Unterstützung für das Bistum",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3508: Account(
        number=3508,
        description="Ökumene",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3509: Account(
        number=3509,
        description="Heizung",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3510: Account(
        number=3510,
        description="Strom",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3511: Account(
        number=3511,
        description="Wasser",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3512: Account(
        number=3512,
        description="Reinigung",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3513: Account(
        number=3513,
        description="Straßenreinigung",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3514: Account(
        number=3514,
        description="Garten- und Winterdienst",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3515: Account(
        number=3515,
        description="Rundfunk",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3516: Account(
        number=3516,
        description="Instandhaltung",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3517: Account(
        number=3517,
        description="Bau",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3518: Account(
        number=3518,
        description="Gebäudeversicherung",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3519: Account(
        number=3519,
        description="Büromaterial",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3520: Account(
        number=3520,
        description="Versand",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3521: Account(
        number=3522,
        description="Telefon & Internet",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3523: Account(
        number=3523,
        description="Druck",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3524: Account(
        number=3524,
        description="Haftpflichtversicherung",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    # Hier fehlt die Öffentlichkeitsarbeit: Website, Plakate
    4100: Account(
        number=4100,
        description="Zinserträge",
        type=AccountType.REVENUE_ACCOUNT,
    ),
    4500: Account(
        number=4500,
        description="Bankgebühren",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    5100: Account(
        number=5100,
        description="Einnahmen im Zweckbetrieb",
        type=AccountType.REVENUE_ACCOUNT,
    ),
    5500: Account(
        number=5500,
        description="Ausgaben im Zweckbetrieb",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    6100: Account(
        number=6100,
        description="Einnahmen im wirtschaftlicher Geschäftsbetrieb",
        type=AccountType.REVENUE_ACCOUNT,
    ),
    6500: Account(
        number=6500,
        description="Ausgaben im wirtschaftlicher Geschäftsbetrieb",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    9000: Account(
        number=9000,
        description="Vorjahresvermögen",
        type=AccountType.LIABILITY_ACCOUNT,
    ),
}
