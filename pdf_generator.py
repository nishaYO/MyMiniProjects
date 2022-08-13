import webbrowser

from fpdf import FPDF

# pdf created
pdf = FPDF()
# a page added in the pdf created
pdf.add_page()

# adding image
pdf.image("home.png", w=20, h=20)

# setting the style
pdf.set_font(family="Times", size=20, style='I')

# fpdf uses cells to write a text
pdf.cell(w=0, h=100, txt='This is a pdf file.', border=1, ln=1, align="C")
pdf.cell(w=0, h=100, txt='this is the body section.', border=0)

# border 1 shows the boxes and 0 doesn't.


# giving the file name
pdf.output("sample.pdf")

# automatic opening of the pdf
webbrowser.open("sample.pdf")
