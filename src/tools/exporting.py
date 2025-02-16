import os

from docx import Document
from win32com import client

from models.record import Record


def _create_document():
    doc = Document()

    doc.add_paragraph("Einfacher Text")
    doc.add_heading("Überschrift", level=1)

    paragraph = doc.add_paragraph()
    run = paragraph.add_run("Formatierter Text")
    run.bold = True
    run.italic = True

    table = doc.add_table(rows=2, cols=2)
    cell = table.cell(0, 0)
    cell.text = "Zelle 1"

    doc.save("dokument.docx")


def _add_records_table(doc: Document, records: [Record]):

    table = doc.add_table(rows=len(records), cols=5)
    cell = table.cell(0, 0)
    cell.text = "Zelle 1"


def _print():
    doc_path = os.path.join(os.getcwd(), "dokument.docx")
    word = client.Dispatch("Word.Application")
    doc = word.Documents.Open(doc_path)
    doc.SaveAs(doc_path + ".pdf", FileFormat=17)  # FileFormat=17 is for PDF
    doc.Close()
    word.Quit()


def _create_daybook_report(daybook):
    pass


def _create_donors_report(donors):
    pass


def _create_accounts_report(accounts):
    pass


def export(report):
    _create_accounts_report(report.accounts)
    _create_daybook_report(report.daybook)
    _create_donors_report(report.donors)
