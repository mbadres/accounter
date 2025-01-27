from configurations.accounts import accounts
from models.account_type import AccountType
from models.record import Record


class Donor:

    def __init__(
        self,
        first_name: str,
        last_name: str,
        address_addition: str,
        street: str,
        number: str,
        postal_code: str,
        city: str,
        country: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.address_addition = address_addition
        self.street = street
        self.number = number
        self.postal_code = postal_code
        self.city = city
        self.country = country
        self.records: [Record] = []

    @property
    def donations_sum(self):
        sum = 0
        for record in self.records:
            if accounts[record.credit_account].type == AccountType.REVENUE_ACCOUNT:
                sum += record.amount
            elif accounts[record.debit_account].type == AccountType.REVENUE_ACCOUNT:
                sum -= record.amount

        return sum
