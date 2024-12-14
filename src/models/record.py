from datetime import date


class Record:
    def __init__(
        self,
        number: int,
        date: date,
        description: str,
        amount: int,
        debit_account: int,
        credit_account: int,
        reference: str = "",
    ) -> None:
        self.number = number
        self.date = date
        self.description = description
        self.amount = amount
        self.debit_account = debit_account
        self.credit_account = credit_account
        self.reference = reference

    def __str__(self) -> str:
        return f"{self.number}, {self.date}, {self.description}, {self.amount}, {self.debit_account}, {self.credit_account}, {self.reference}"
