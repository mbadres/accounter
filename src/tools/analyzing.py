from data.accounts import accounts
from models.account_type import AccountType
from models.daybook import daybook
from models.record import Record


def analyze(records: [Record]):

    for record in records:
        print(record)

        debit_account = accounts[record.debit_account]
        credit_account = accounts[record.credit_account]

        # Add the record to the daybook.
        daybook.add(record)

        # Add record to its belonging accounts.
        debit_account.records.append(record)
        credit_account.records.append(record)

        # Check if the record is a donation.
        if (
            credit_account.type == AccountType.REVENUE_ACCOUNT
            and credit_account.class_number == 3
        ) or (
            debit_account.type == AccountType.REVENUE_ACCOUNT
            and debit_account.class_number == 3
        ):

            # Add record to its belonging donors.
            ...

    # Create a budget plan.
    return ""
