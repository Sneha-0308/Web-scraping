import PyPDF2
# TODO 1 : create the existing pdf file object by opening those files
pdfobj1 = open('pdf1.pdf','rb')
pdfobj2 = open('pdf2.pdf','rb')

# TODO 2 : create reader objects for those pdf objects
read1 = PyPDF2.PdfFileReader(pdfobj1)
read2 = PyPDF2.PdfFileReader(pdfobj2)

# TODO 3 : create new blank pdf write object
pdfWrite = PyPDF2.PdfFileWriter()

# TODO 4: Write the content from existing pdf to the new pdf
for pageno in range(read1.numPages):
    pageObj1 = read1.getPage(pageno)
    pdfWrite.write(pageObj1)

for pageno in range(read2.numPages):
    pageObj2 = read2.getPage(pageno)
    pdfWrite.write(pageObj2)

# TODO 5 : now write the content whatever the write object holding into the new pdf
pdfoutput = open('CombineContent.pdf', 'wb')
pdfWrite.write(pdfoutput)
#  TODO 6 : close all pdfs
pdfobj1.close()
pdfobj2.close()
pdfoutput.close()
