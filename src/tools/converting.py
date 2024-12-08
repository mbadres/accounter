from typing import Any

from pandas import concat, DataFrame

from models.record import Record


def _map(index: int, row: tuple[Any, ...]) -> Record:
    # TODO Implement.
    return Record(
        index,
        row.date,
        row.description,
        row.amount,
        row.debit_account,
        row.credit_account,
        row.reference,
    )


def convert(
    activities_books: list[DataFrame], cash_books: list[DataFrame]
) -> list[Record]:
    # Merge the dataframes into one data sorted dataframe.
    data = concat(activities_books, ignore_index=True).sort_values("date")

    # Convert the new dataframe into a list of accounting records.
    records: list[Record] = []
    index = 0
    for row in data.itertuples():
        index += 1
        record = _map(index, row)
        records.append(record)

    return records
