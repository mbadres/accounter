from models.account import Account
from models.account_type import AccountType

accounts = {
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
    3200: Account(
        number=3200,
        description="Kollekte",
        type=AccountType.REVENUE_ACCOUNT,
    ),
    3300: Account(
        number=3300,
        description="Öffentliche Zuschüsse",
        type=AccountType.REVENUE_ACCOUNT,
    ),
    3310: Account(
        number=3310,
        description="Kirchliche Zuschüsse",
        type=AccountType.REVENUE_ACCOUNT,
    ),
    4100: Account(
        number=4100,
        description="Pfarrdienst",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    4110: Account(
        number=4110,
        description="Materialien (z.B. Kerzen Wein Bücher)",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    4200: Account(
        number=4200,
        description="Materialien für die Sonntagschule oder ähnliches",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    4210: Account(
        number=4210,
        description="Bezuschussung von Treffen Ausflügen und anderen Unternehmungen",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    4220: Account(
        number=4220,
        description="Gemeinschaftsessen",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    4230: Account(
        number=4230,
        description="Fahrtkostenerstattung für Seelsorge",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    4300: Account(
        number=4300,
        description="Unterstützung für das Bistum)",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    4310: Account(
        number=4310,
        description="Ökumene",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    4400: Account(
        number=4400,
        description="Heizung",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    4410: Account(
        number=4410,
        description="Strom",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    4420: Account(
        number=4420,
        description="Wasser",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    4430: Account(
        number=4430,
        description="Reinigung",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    4440: Account(
        number=4440,
        description="Instandhaltung",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    4450: Account(
        number=4450,
        description="Bau",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    4500: Account(
        number=4500,
        description="Gebäudeversicherung",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    4510: Account(
        number=4510,
        description="Haftpflichtversicherung",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    4600: Account(
        number=4600,
        description="Büromaterial",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    4610: Account(
        number=4610,
        description="Porto",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    4620: Account(
        number=4620,
        description="Telefon & Internet",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    4630: Account(
        number=4630,
        description="Druckkosten",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    5100: Account(
        number=5100,
        description="Zinserträge",
        type=AccountType.REVENUE_ACCOUNT,
    ),
    5500: Account(
        number=5500,
        description="Bankgebühren",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    6100: Account(
        number=6100,
        description="Einnahmen Zweckbetrieb",
        type=AccountType.REVENUE_ACCOUNT,
    ),
    6500: Account(
        number=6500,
        description="Ausgaben Zweckbetrieb",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    7100: Account(
        number=7100,
        description="Einnahmen Wirtschaftlicher Geschäftsbetrieb",
        type=AccountType.REVENUE_ACCOUNT,
    ),
    7500: Account(
        number=7500,
        description="Ausgaben Wirtschaftlicher Geschäftsbetrieb",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
}
