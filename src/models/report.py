from models.account import Account
from models.daybook import Daybook
from models.donor import Donor


class Report:
    def __init__(
        self, year: int, accounts: [Account], daybook: Daybook, donors: [Donor]
    ):
        self.year = year
        self.accounts = accounts
        self.daybook = daybook
        self.donors = donors
