import PyPDF2
pd = open('thinkpython.pdf', 'rb')
re = PyPDF2.PdfFileReader(pd)
re.numPages
out = re.getPage(0)
out.extractText()
print (out)
