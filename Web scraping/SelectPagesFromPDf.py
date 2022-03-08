# Project: Combining Select Pages from Many PDFs

#  TODO : Find all the pdf in directory
import PyPDF2,os
pdfFiles = []  # to store the all pdfs from the folder
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)  # insert or append the .pdf files in list

pdfFiles.sort(key = str.lower)  # sorting based on ascii
# NOTE : while creating the reader object we have to pass
# the file object because reader object is specific to specific file
# but for write object no need t pass the file because only one write
# object is required to write all files there is no specific write object for differrent files

pdfwriter = PyPDF2.PdfFileWriter()


# TODO: Loop through all the PDF files.
# while looping through the whole list for each file create file onject and file reader object
for filename in pdfFiles:
    pdfFileObj = open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # TODO: Loop through all the pages (except the first) and add them.
    for pageno in range(1,pdfReader.numPages):
        pageobj = pdfReader.getPage(pageno)
        pdfwriter.write(pageobj)
# TODO: Save the resulting PDF to a file
pdfOutput = open('final.pdf','wb')
pdfwriter.write(pdfOutput)
pdfOutput.close()