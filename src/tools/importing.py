from pathlib import Path

from pandas import DataFrame, read_csv

from data.settings import activities_books_directory, delimiter, date_tag


def _check(path: Path) -> None:
    """
    This function checks that the directory exist.
    :param path: The directory path
    :raise: FileNotFoundError if the specified directory does not exist
    """
    if not path.exists():
        raise FileNotFoundError(f"{path} does not exist!")


def _import(path) -> list[DataFrame]:
    """
    Import all CSV files.
    :param path: Path of directory
    :return: List of dataframes
    """
    _check(path)

    dataframes: list[DataFrame] = []

    for file in path.glob("*.csv"):
        dataframes.append(
            read_csv(file, parse_dates=[date_tag], dayfirst=True, delimiter=delimiter)
        )

    return dataframes


def read(path: str) -> tuple[list[DataFrame], list[DataFrame]]:
    """
    Import all necessary CSV files.
    :param path: path of directory where the cash book directory and activities_books directory exist
    :return: Tuple of list of dataframes
    """
    path = Path(path)
    _check(path)

    activities_books = _import(path / activities_books_directory)
    # cash_books = _import(path / cash_book_directory)
    cash_books = _import(path / activities_books_directory)

    return activities_books, cash_books
