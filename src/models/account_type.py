from enum import Enum


class AccountType(Enum):
# Aktickonto = asset account
# Passivkonto = liability account
    """Type of the account"""

    INCOME = "Einnahme"
    EXPENSE = "Ausgabe"
