from fpdf import FPDF

pdf = FPDF('p','mm','Letter')
pdf.add_page()

pdf.set_font('times','B',16)

pdf.cell(40,10,'Hello World!')

pdf.output('pdf_1.pdf')