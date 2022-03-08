# python -m pip install pypdf2   ==> command to install PyPDF2
# PyPDF2 does not extract images, charts or other media from PDF documents but it can extract text adn returns it as Python String

import PyPDF2    #import PyPDF2 module
pdffileobj = open('test.pdf', 'rb')   # create the pdf object by opening the pdf in read mode
pdfReader = PyPDF2.PdfFileReader(pdffileobj)  # read the pdf by using pdf object
print(pdfReader.numPages)     # find the number of pages so that you can extract those padf page only
pageObj = pdfReader.getPage(0) # get content of a particular page by mentioning the index of page starts from 0
print(pageObj.extractText()) # print the content of that page by extract method
pdffileobj.close()



'''
1] import
2] create pdf object
3] create reader object
4] count number of pages in that object
5] get a specific page
6] then extract content from that page'''