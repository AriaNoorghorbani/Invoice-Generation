from glob import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob("Invoices/*.xlsx")

#files in filepaths
for filepath in filepaths:
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=16)
    Invoice_nr = Path(filepath).stem.split("-")[0]
    pdf.cell(w=50, h=8, txt=f"Invoice Nr.{Invoice_nr}")
    pdf.output(f"PDFs/{Invoice_nr}.pdf")