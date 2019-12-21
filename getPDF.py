# This is just to get the PDFs from a directory

import PyPDF2
import glob

pdf_dir = "/home/scott/projects/RedTideResearch/dataHarvests"

pdf_files = glob.glob("%s/*.pdf" % pdf_dir)
for file in pdf_files:
    print(file)
    open(file, 'rb')
    print(PyPDF2.PdfFileReader(file))



'''   
pdfFileObj = open("/home/scott/projects/RedTideResearch/dataHarvests/HAB-Mgmt-Response-2008_233764.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)

pageObj = pdfReader.getPage(10)
pageObj.extractText
'''