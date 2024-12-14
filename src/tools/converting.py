from datetime import date
from typing import Any

from pandas import concat, DataFrame

from data.settings import date_tag, placeholder
from data.temlpates import templates
from models.record import Record


def _create_general_donation_record(
    index: int, date: date, amount: int, name: str
) -> Record:
    map = templates["general_donation"]
    print(name)
    return Record(
        number=index,
        date=date,
        description=map["description"].replace(placeholder, name),
        amount=amount,
        debit_account=map["debit_account"],
        credit_account=map["credit_account"],
    )


def _shrink(data: DataFrame) -> DataFrame:
    return data[
        [
            "IBAN Auftragskonto",
            "Buchungstag",
            "Name Zahlungsbeteiligter",
            "Buchungstext",
            "Verwendungszweck",
            "Betrag",
            "Saldo nach Buchung",
        ]
    ]


def _map(index: int, row: tuple[Any, ...]) -> Record:
    # TODO Implement.
    if True:
        return _create_general_donation_record(
            index=index,
            date=row["Buchungstag"],
            amount=row["Betrag"],
            name=row["Name Zahlungsbeteiligter"],
        )
    return Record(
        number=index,
        date=row["Buchungstag"],
        description="row.description",
        amount=row["Betrag"],
        debit_account="row.debit_account",
        credit_account="row.credit_account",
        reference="row.reference",
    )


def convert(
    activities_books: list[DataFrame], cash_books: list[DataFrame]
) -> list[Record]:
    # Merge the dataframes into one data sorted dataframe.
    data = concat(activities_books, ignore_index=True).sort_values(date_tag)

    # Convert the new dataframe into a list of accounting records.
    records: list[Record] = []
    index = 0
    for _, row in data.iterrows():
        index += 1
        record = _map(index, row)
        records.append(record)

    return records
