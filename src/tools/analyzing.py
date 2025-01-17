from data.accounts import accounts
from models.record import Record


def analyze(daybook: [Record]):

    # Add records to their belonging accounts.
    for record in daybook:
        print(record)

        accounts[record.debit_account].records.append(record)
        accounts[record.credit_account].records.append(record)

    return ""
