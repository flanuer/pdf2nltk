# This is just to get the PDFs from a directory


import PyPDF2
import glob

pdf_dir = "/home/scott/projects/RedTideResearch/dataHarvests"

pdf_files = glob.glob("%s/*.pdf" % pdf_dir)
for file in pdf_files:
    print(file)
