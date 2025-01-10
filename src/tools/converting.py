from datetime import datetime

from pandas import concat, DataFrame, Series

from data.settings import date_tag, placeholder
from data.temlpates import templates
from models.record import Record


def _create_record(template: str, date: datetime, amount: int, name: str) -> Record:
    map = templates[template]
    return Record(
        date=date,
        description=map["description"].replace(placeholder, str(name)),
        amount=amount,
        debit_account=map["debit_account"],
        credit_account=map["credit_account"],
    )


def _begin(data: list[DataFrame]) -> list[Record]:
    data.groupby("IBAN Auftragskonto").agg(
        {
            "Buchungstag": "min",
            "Betrag": "sum",
            "Saldo nach Buchung": "mean",
        }
    )
    return []


def _begin(activities_books: list[DataFrame]) -> list[Record]:
    """Determine the opening balance of each activities_books."""

    for book in activities_books:
        iban = book.iloc[-1]["IBAN Auftragskonto"]
        account_description = book.iloc[-1]["Bezeichnung Auftragskonto"]
        year = datetime.strptime(book.iloc[-1]["Buchungstag"], "%d.%m.%Y").year
        result = float(book.iloc[-1]["Saldo nach Buchung"].replace(",", "."))
        amount = float(book.iloc[-1]["Betrag"].replace(",", "."))
        beginning = result - amount

        yield Record(
            date=datetime(year, 1, 1),
            description="Anfangsbestand",
            amount=beginning,
            debit_account=0,
            credit_account=2220,
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


def _map(row: Series) -> Record:
    # TODO Implement.
    if True:
        return _create_record(
            template="general_donation",
            date=row["Buchungstag"],
            amount=row["Betrag"],
            name=row["Name Zahlungsbeteiligter"],
        )

    return Record(
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
    _begin(activities_books)

    # Merge the dataframes into one data sorted dataframe.
    data = concat(activities_books, ignore_index=True).sort_values(date_tag)

    # Convert the new dataframe into a list of accounting records.
    records: list[Record] = []
    for _, row in data.iterrows():
        record = _map(row)
        records.append(record)

    return records
