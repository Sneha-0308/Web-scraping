import PyPDF2

pdfobj = open('test.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfobj)
print(pdfReader.numPages)

print(pdfReader.isEncrypted)

# TODO : pdfReader.decrypt('password')  Give the correct password to decrypt
# TODO : pdfReader.encrypt('password)
# readerobj.isEncrypted
#  if it is True ===> it is encrypted and you can not extract text.
#  If you want to extract text from encrypted pdf you have to first
#  decrypt the pdf

# If it is False then you can get the content by using extractText function
pageobj = pdfReader.getPage(0)
print(pageobj.extractText())

