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

    @property
    def beginning_inventory(self):
        for record in self.records:
            if record.credit_account >= 9000:
                return record.amount

        return 0

    @property
    def debit_credit_sums(self):
        debit_sum = 0
        credit_sum = 0
        for record in self.records:
            if self.number == record.debit_account:
                debit_sum += record.amount
            else:
                credit_sum += record.amount

        return debit_sum, credit_sum

    @property
    def balance(self):
        debit_sum, credit_sum = self.debit_credit_sums

        if self.type.is_debit_increase():
            return debit_sum - credit_sum
        else:
            return credit_sum - debit_sum
