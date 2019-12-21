import PyPDF2
import glob

PDF_DIRECTORY = "/home/scott/projects/RedTideResearch/dataHarvests"

pdf_files = glob.glob("%s/*.pdf" % PDF_DIRECTORY)
for file in pdf_files:
    print(file)
    open(file, 'rb')
    title = repr(PyPDF2.PdfFileReader(file))
    print(title)
    '''with open(title, mode='rb) as f:
        reader = PyPDF2.PdfFileReader(f)
        page = reader.getPage(5)
        print(page.extractText())
        print('.....................................')



FILE_PATH = '/home/scott/projects/RedTideResearch/dataHarvests/HAB-Mgmt-Response-2008_233764.pdf'

with open(FILE_PATH, mode='rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    page = reader.getPage(10)
    print(page.extractText())


pdf_dir = "/home/scott/projects/RedTideResearch/dataHarvests"

pdf_files = glob.glob("%s/*.pdf" % pdf_dir)
for file in pdf_files:
    print(file)
    open(file, 'rb')
    print(PyPDF2.PdfFileReader(file))
'''