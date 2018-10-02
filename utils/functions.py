import os
import shutil
from PyPDF2 import PdfFileReader,PdfFileWriter
def function_split(ar,path):
    inputPdf=open(path,'rb')
    pdfReader=PdfFileReader(inputPdf)
    #print "No. of pages ",pdfReader.getNumPages()

    for i in range(pdfReader.numPages):
        output = PdfFileWriter()
        output.addPage(pdfReader.getPage(i))
        with open(os.path.join("splitted//%s.pdf") % (i+1), "wb") as outputStream:
            output.write(outputStream)
    inputPdf.close()
    os.remove(path)
    shutil.make_archive(os.path.join("todownload//download"),'zip',os.path.join('splitted'))
    return True