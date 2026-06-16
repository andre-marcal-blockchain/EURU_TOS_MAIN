from pathlib import Path

from docx import Document
from docx.table import Table as DocxTable
from docx.text.paragraph import Paragraph
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageTemplate,
    Paragraph as PdfParagraph,
    Spacer,
    Table as PdfTable,
    TableStyle,
)
from xml.sax.saxutils import escape


ROOT = Path(r"C:\Users\andre\Desktop\EURU TOS MAIN")
DOCX = ROOT / "output" / "pdf" / "Caso_Practico_Final_Ciberseguridad_Resuelto.docx"
PDF = ROOT / "output" / "pdf" / "Caso_Practico_Final_Ciberseguridad_Resuelto.pdf"

FONT_DIR = Path(r"C:\Windows\Fonts")
for name, file_name in (
    ("Calibri", "calibri.ttf"),
    ("Calibri-Bold", "calibrib.ttf"),
    ("Calibri-Italic", "calibrii.ttf"),
):
    file_path = FONT_DIR / file_name
    if file_path.exists():
        pdfmetrics.registerFont(TTFont(name, str(file_path)))

BASE = "Calibri" if "Calibri" in pdfmetrics.getRegisteredFontNames() else "Helvetica"
BOLD = "Calibri-Bold" if "Calibri-Bold" in pdfmetrics.getRegisteredFontNames() else "Helvetica-Bold"
ITALIC = "Calibri-Italic" if "Calibri-Italic" in pdfmetrics.getRegisteredFontNames() else "Helvetica-Oblique"


def iter_blocks(parent):
    body = parent.element.body
    for child in body.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield DocxTable(child, parent)


def inline_markup(paragraph):
    chunks = []
    for run in paragraph.runs:
        text = escape(run.text).replace("\n", "<br/>")
        if not text:
            continue
        if run.bold:
            text = f"<b>{text}</b>"
        if run.italic:
            text = f"<i>{text}</i>"
        if run.underline:
            text = f"<u>{text}</u>"
        chunks.append(text)
    return "".join(chunks) or escape(paragraph.text)


styles = getSampleStyleSheet()
body = ParagraphStyle(
    "Body",
    fontName=BASE,
    fontSize=10.3,
    leading=12.8,
    textColor=colors.HexColor("#222222"),
    spaceAfter=6,
)
bullet = ParagraphStyle(
    "Bullet",
    parent=body,
    leftIndent=22,
    firstLineIndent=-10,
    bulletIndent=7,
    spaceAfter=5,
)
h1 = ParagraphStyle(
    "H1",
    fontName=BOLD,
    fontSize=15,
    leading=18,
    textColor=colors.HexColor("#2E74B5"),
    spaceBefore=12,
    spaceAfter=7,
    keepWithNext=True,
)
h2 = ParagraphStyle(
    "H2",
    fontName=BOLD,
    fontSize=12.5,
    leading=15,
    textColor=colors.HexColor("#2E74B5"),
    spaceBefore=10,
    spaceAfter=5,
    keepWithNext=True,
)
title = ParagraphStyle(
    "Title",
    fontName=BOLD,
    fontSize=23,
    leading=27,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#0B2545"),
    spaceBefore=18,
    spaceAfter=7,
)
subtitle = ParagraphStyle(
    "Subtitle",
    fontName=BOLD,
    fontSize=14,
    leading=17,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#2E74B5"),
    spaceAfter=4,
)
small_center = ParagraphStyle(
    "SmallCenter",
    fontName=ITALIC,
    fontSize=10.5,
    leading=13,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#5A636E"),
    spaceAfter=14,
)
question = ParagraphStyle(
    "Question",
    fontName=BOLD,
    fontSize=10,
    leading=12.5,
    textColor=colors.HexColor("#0B2545"),
)
table_text = ParagraphStyle(
    "TableText",
    fontName=BASE,
    fontSize=8.2,
    leading=10,
    textColor=colors.HexColor("#222222"),
)
table_head = ParagraphStyle(
    "TableHead",
    fontName=BOLD,
    fontSize=8.5,
    leading=10,
    alignment=TA_CENTER,
    textColor=colors.white,
)
meta_text = ParagraphStyle(
    "Meta",
    fontName=BASE,
    fontSize=9.2,
    leading=11,
    textColor=colors.HexColor("#0B2545"),
)


def draw_page(canvas, doc):
    canvas.saveState()
    canvas.setFont(BASE, 8)
    canvas.setFillColor(colors.HexColor("#5A636E"))
    canvas.drawRightString(letter[0] - 0.72 * inch, letter[1] - 0.38 * inch, "Fundamentos y Estrategias Avanzadas de Ciberseguridad")
    canvas.drawCentredString(letter[0] / 2, 0.36 * inch, f"Caso práctico final  |  Página {doc.page}")
    canvas.restoreState()


pdf = BaseDocTemplate(
    str(PDF),
    pagesize=letter,
    rightMargin=0.78 * inch,
    leftMargin=0.78 * inch,
    topMargin=0.62 * inch,
    bottomMargin=0.58 * inch,
    title="Caso práctico final de ciberseguridad resuelto",
    author="Alumno/a",
)
frame = Frame(pdf.leftMargin, pdf.bottomMargin, pdf.width, pdf.height, id="normal")
pdf.addPageTemplates([PageTemplate(id="main", frames=frame, onPage=draw_page)])

docx = Document(DOCX)
story = []
opening_count = 0

for block in iter_blocks(docx):
    if isinstance(block, Paragraph):
        text = block.text.strip()
        if not text:
            continue
        style_name = block.style.name if block.style else "Normal"
        markup = inline_markup(block)
        if opening_count == 0 and text == "CASO PRÁCTICO FINAL":
            story.append(PdfParagraph(markup, title))
            opening_count += 1
        elif opening_count == 1 and text.startswith("Fundamentos y Estrategias"):
            story.append(PdfParagraph(markup, subtitle))
            opening_count += 1
        elif opening_count == 2 and text.startswith("Informe de seguridad"):
            story.append(PdfParagraph(markup, small_center))
            opening_count += 1
        elif style_name == "Heading 1":
            story.append(PdfParagraph(markup, h1))
        elif style_name == "Heading 2":
            story.append(PdfParagraph(markup, h2))
        elif style_name.startswith("List Bullet"):
            story.append(PdfParagraph(markup, bullet, bulletText="•"))
        else:
            story.append(PdfParagraph(markup, body))
    else:
        raw = [[cell.text.strip() for cell in row.cells] for row in block.rows]
        if not raw:
            continue
        cols = len(raw[0])
        if cols == 1:
            content = [[PdfParagraph(escape(raw[0][0]), question)]]
            t = PdfTable(content, colWidths=[pdf.width], hAlign="LEFT")
            t.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F4F6F9")),
                        ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#D4DBE4")),
                        ("LEFTPADDING", (0, 0), (-1, -1), 8),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                        ("TOPPADDING", (0, 0), (-1, -1), 7),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                    ]
                )
            )
            story.extend([t, Spacer(1, 7)])
        elif cols == 2:
            content = [[PdfParagraph(escape(c), meta_text) for c in row] for row in raw]
            t = PdfTable(content, colWidths=[pdf.width / 2] * 2, hAlign="LEFT")
            t.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#E8EEF5")),
                        ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#C8D2DE")),
                        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 7),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                        ("TOPPADDING", (0, 0), (-1, -1), 6),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
                    ]
                )
            )
            story.extend([t, Spacer(1, 5)])
        else:
            if cols == 4:
                widths = [1.16 * inch, 1.92 * inch, 1.56 * inch, 1.56 * inch]
            else:
                widths = [1.15 * inch, 3.05 * inch, 2.0 * inch]
            content = []
            for row_idx, row in enumerate(raw):
                row_style = table_head if row_idx == 0 else table_text
                content.append([PdfParagraph(escape(c), row_style) for c in row])
            t = PdfTable(content, colWidths=widths, repeatRows=1, hAlign="LEFT")
            t.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#2E74B5")),
                        ("GRID", (0, 0), (-1, -1), 0.45, colors.HexColor("#AEB9C6")),
                        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 5),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                        ("TOPPADDING", (0, 0), (-1, -1), 5),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
                    ]
                )
            )
            story.extend([t, Spacer(1, 6)])

pdf.build(story)
print(PDF)
