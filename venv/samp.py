# import aspose.pdf as ap
#
# input_pdf = r"C:\Users\kaushik\PycharmProjects\moodle_doc\\venv\\result.html"
# output_pdf = "output0.pdf"
# options = ap.HtmlLoadOptions()
# document = ap.Document(input_pdf, options)
# document.save(output_pdf)

import pdfkit

l=[]

for i in range(11):
    op_file = 'result' + str(i) + '.html'
    l.append(op_file)


pdfkit.from_file(l, "mod5.pdf", options={"enable-local-file-access": ""})