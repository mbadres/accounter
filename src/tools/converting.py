from datetime import datetime

from pandas import concat, DataFrame, Series

from data.mappings import mappings
from data.settings import date_tag, placeholder, no_template
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
        if iban[-2:] == "20":
            debit_account = 1110
        elif iban[-2:] == "01":
            debit_account = 1120
        else:
            debit_account = 1100

        year = datetime.strptime(book.iloc[-1]["Buchungstag"], "%d.%m.%Y").year
        result = float(book.iloc[-1]["Saldo nach Buchung"].replace(",", "."))
        amount = float(book.iloc[-1]["Betrag"].replace(",", "."))
        beginning = result - amount

        yield Record(
            date=datetime(year, 1, 1),
            description="Eröffnungsbuchung",
            amount=beginning,
            debit_account=debit_account,
            credit_account=9000,
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

    template = no_template
    for mapping in mappings:
        condition = True
        condition = (
            condition and row["IBAN Auftragskonto"] == mapping["IBAN Auftragskonto"]
        )
        condition = (
            condition
            and row["Name Zahlungsbeteiligter"] == mapping["Name Zahlungsbeteiligter"]
        )
        condition = condition and row["Buchungstext"] == mapping["Buchungstext"]
        condition = condition and row["Verwendungszweck"] == mapping["Verwendungszweck"]

        if condition:
            template = mapping["Buchungsvorlage"]
            break

    return _create_record(
        template=template,
        date=datetime.strptime(row["Buchungstag"], "%d.%m.%Y"),
        amount=row["Betrag"],
        name=row["Name Zahlungsbeteiligter"],
    )


def convert(
    activities_books: list[DataFrame], cash_books: list[DataFrame]
) -> list[Record]:
    records = list(_begin(activities_books))

    # Merge the dataframes into one data sorted dataframe.
    data = concat(activities_books, ignore_index=True).sort_values(date_tag)

    for _, row in data.iterrows():
        record = _map(row)
        records.append(record)

    return records
