from enum import Enum


class AccountType(Enum):
    """Type of the account"""

    # Balance Sheet Accounts (Bestandskonten)
    ASSET_ACCOUNT = "Aktivkonto"
    LIABILITY_ACCOUNT = "Passivkonto"

    # Profit and Loss Accounts / Income Statement Accounts (Erfolgskonten)
    REVENUE_ACCOUNT = "Ertragskonto"
    EXPENSE_ACCOUNT = "Aufwandskonto"

    # Accrual Accounts (Abgrenzungskonten)
    PREPAID_EXPENSES = "Aktive Rechnungsabgrenzung"
    DEFERRED_INCOME = "Passive Rechnungsabgrenzung"

    # Drawing Accounts (Privatkonten)
    PROPRIETOR_S_ACCOUNT = "Privatkonto"

    # Suspense Accounts (Zwischenkonten)
    TRANSIT_ACCOUNT = "Zwischenkonto"

    def is_debit_increase(self) -> bool:
        """
        This method indicates how the account type is effecting the balance growth.
        :return: True if account balance shall be raise if debit is increased.
        """
        return self in [
            AccountType.ASSET_ACCOUNT,
            AccountType.EXPENSE_ACCOUNT,
            AccountType.PREPAID_EXPENSES,
            AccountType.PROPRIETOR_S_ACCOUNT,
            AccountType.TRANSIT_ACCOUNT,
        ]
