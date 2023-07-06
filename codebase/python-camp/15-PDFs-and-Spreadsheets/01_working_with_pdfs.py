
# Reading PDFs with Python

# import PyPDF2

# # Notice we read it as a binary with 'rb'
# f = open('Working_Business_Proposal.pdf','rb')

# pdf_reader = PyPDF2.PdfReader(f)

# # print(pdf_reader)

# # print(len(pdf_reader.pages))

# page_number = 0
# page_one = pdf_reader.pages[0]

# page_one_text = page_one.extract_text()

# print(page_one_text)

# f.close()

# Adding to PDFs

import PyPDF2

# Notice we read it as a binary with 'rb'
f = open('Working_Business_Proposal.pdf','rb')

pdf_reader = PyPDF2.PdfReader(f)

# print(pdf_reader)

# print(len(pdf_reader.pages))

page_number = 0
page_one = pdf_reader.pages[0]

pdf_writer = PyPDF2.PdfWriter()

pdf_writer.add_page(page_one);

pdf_output = open("Some_New_Doc.pdf","wb")

pdf_writer.write(pdf_output)

f.close()

# Simple Example


f = open('Working_Business_Proposal.pdf','rb')

# List of every page's text.
# The index will correspond to the page number.
pdf_text = []

pdf_reader = PyPDF2.PdfReader(f)

for p in range(len(pdf_reader.pages)):
    
    page = pdf_reader.pages[0]
    
    pdf_text.append(page.extract_text())
    
print(pdf_text)