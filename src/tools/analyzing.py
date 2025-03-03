from data.accounts import accounts
from models.account_type import AccountType
from models.daybook import Daybook
from models.donor import Donor
from models.record import Record
from models.report import Report


def analyze(records: [Record]):
    year = records[0].date.year
    daybook = Daybook()
    donors: [str, Donor] = {}

    for record in records:

        if record.date.year != year:
            print(record)
            print(year)
            raise ValueError("ERROR: Record does not belong to finance year.")

        # Add the record to the daybook.
        daybook.add(record)

        debit_account = accounts[record.debit_account]
        credit_account = accounts[record.credit_account]

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
            if record.description not in donors:
                donors[record.description] = Donor(
                    first_name="",
                    last_name="",
                    address_addition="",
                    street="",
                    number="",
                    postal_code="",
                    city="",
                    country="",
                )
            donors[record.description].records.append(record)

    # Create a budget plan.
    return Report(year, accounts, daybook, donors)
