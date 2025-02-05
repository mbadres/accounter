from data.settings import path
from tools.analyzing import analyze
from tools.converting import convert
from tools.exporting import export
from tools.importing import read

if __name__ == "__main__":
    # setup/load
    activities_books, cash_books = read(path)
    daybook = convert(activities_books, cash_books)
    reports = analyze(daybook)
    export(reports)
