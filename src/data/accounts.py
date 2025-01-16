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
    3500: Account(
        number=3500,
        description="Pfarrdienst",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3510: Account(
        number=3510,
        description="Materialien für den Gottesdienst",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3520: Account(
        number=5320,
        description="Materialien für die Sonntagschule oder ähnliches",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3530: Account(
        number=5330,
        description="Bezuschussung von Treffen Ausflügen und anderen Unternehmungen",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3540: Account(
        number=5340,
        description="Gemeinschaftsessen",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3550: Account(
        number=5350,
        description="Fahrtkostenerstattung für Seelsorge",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3600: Account(
        number=3600,
        description="Unterstützung für das Bistum",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3700: Account(
        number=3700,
        description="Ökumene",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3800: Account(
        number=3800,
        description="Heizung",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3810: Account(
        number=3810,
        description="Strom",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3820: Account(
        number=3820,
        description="Wasser",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3830: Account(
        number=3830,
        description="Reinigung",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3840: Account(
        number=3840,
        description="Straßenreinigung",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3850: Account(
        number=3850,
        description="Garten- und Winterdienst",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3860: Account(
        number=3860,
        description="Rundfunk",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3870: Account(
        number=3870,
        description="Instandhaltung",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3880: Account(
        number=3880,
        description="Bau",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3890: Account(
        number=3890,
        description="Gebäudeversicherung",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3900: Account(
        number=3900,
        description="Büromaterial",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3910: Account(
        number=3910,
        description="Versand",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3920: Account(
        number=3920,
        description="Telefon & Internet",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3930: Account(
        number=3930,
        description="Druck",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    3940: Account(
        number=3940,
        description="Haftpflichtversicherung",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
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
        description="Einnahmen Zweckbetrieb",
        type=AccountType.REVENUE_ACCOUNT,
    ),
    5500: Account(
        number=5500,
        description="Ausgaben Zweckbetrieb",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    6100: Account(
        number=6100,
        description="Einnahmen Wirtschaftlicher Geschäftsbetrieb",
        type=AccountType.REVENUE_ACCOUNT,
    ),
    6500: Account(
        number=6500,
        description="Ausgaben Wirtschaftlicher Geschäftsbetrieb",
        type=AccountType.EXPENSE_ACCOUNT,
    ),
    9000: Account(
        number=9000,
        description="Vorjahresvermögen",
        type=AccountType.LIABILITY_ACCOUNT,
    ),
}
