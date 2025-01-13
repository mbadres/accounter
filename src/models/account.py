from data.account_classes import account_classes
from data.account_groups import account_groups
from models.account_type import AccountType
from models.record import Record


class Account:

    def __init__(
        self,
        number: int,
        description: str,
        type: AccountType,
    ) -> None:
        self.number = number
        self.description = description
        self.type = type
        self.records: list[Record] = []

    @property
    def class_number(self):
        return self.number // 1000

    @property
    def class_description(self):
        return account_classes[self.class_number]

    @property
    def group_number(self):
        return self.number // 100 * 10

    @property
    def group_description(self):
        return account_groups[self.group_number]
