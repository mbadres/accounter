from datetime import datetime


class Record:

    _index = 0

    def __init__(
        self,
        date: datetime,
        description: str,
        amount: float,
        debit_account: int,
        credit_account: int,
        reference: str = "",
    ) -> None:
        Record._index += 1
        self.number = Record._index
        self.date = date
        self.description = description
        self.amount = amount
        self.debit_account = debit_account
        self.credit_account = credit_account
        self.reference = reference

    def __str__(self) -> str:
        delimiter = "\t"
        return f"{self.number}{delimiter}{self.date.strftime("%d.%m.%Y")}{delimiter}{self.description}{delimiter}{self.amount}{delimiter}{self.debit_account}{delimiter}{self.credit_account}{delimiter}{self.reference}"
