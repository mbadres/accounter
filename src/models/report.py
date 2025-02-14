from models.account import Account
from models.daybook import Daybook
from models.donor import Donor


class Report:
    def __init__(self, accounts: [Account], daybook: Daybook, donors: [Donor]):
        self.accounts = accounts
        self.daybook = daybook
        self.donors = donors
