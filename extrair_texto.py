from PyPDF2 import PdfReader


reader = PdfReader("data/portugues.pdf")
page = reader.pages[0]
print(page.extract_text())