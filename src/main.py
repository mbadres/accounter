from data.settings import path
from tools.analyzing import analyze
from tools.converting import convert
from tools.exporting import export
from tools.importing import read
from tools.loading import load

if __name__ == "__main__":
    corrections, donations_in_kind, mappings, settings, templates = load()
    activities_books, cash_books = read(path)
    daybook = convert(activities_books, cash_books)
    report = analyze(daybook)
    export(report)
