import os

from docx import Document
from win32com import client


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


def _print():
    doc_path = os.path.join(os.getcwd(), "dokument.docx")
    word = client.Dispatch("Word.Application")
    doc = word.Documents.Open(doc_path)
    doc.SaveAs(doc_path + ".pdf", FileFormat=17)  # FileFormat=17 is for PDF
    doc.Close()
    word.Quit()


def export(reports):
    _create_document()
