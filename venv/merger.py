import os
from PyPDF2 import PdfReader, PdfWriter
def merge_pdfs(l, output):
    paths = []
    for i in range(l):
        paths.append('output' + str(i) + '.pdf')
    pdf_writer = PdfWriter()

    for path in paths:
        pdf_reader = PdfReader(path)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

    op = output + ".pdf"
    with open(op, 'wb') as out:
        pdf_writer.write(out)

    for i in range(l):
        os.remove('output' + str(i)  + '.pdf')

