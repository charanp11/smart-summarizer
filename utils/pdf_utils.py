from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from textwrap import wrap
import fitz # PyMuPDF

def save_summary_as_pdf(summary_text, file_path):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter
    wrapped_text = wrap(summary_text, width=90)
    y = height - 40

    for line in wrapped_text:
        c.drawString(40, y, line)
        y -= 15
        if y < 40:
            c.showPage()
            y = height - 40

    c.save()
    return file_path

def extract_text_from_pdf(filepath):
    text = ""
    with fitz.open(filepath) as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()
