import os
import shutil
from PyPDF2 import PdfFileReader,PdfFileWriter,PdfFileMerger


def function_split(single,rng,path):
    #to remove previously splitted files
    shutil.rmtree('splitted')
    os.mkdir('splitted')

    inputPdf=open(path,'rb')
    pdfReader=PdfFileReader(inputPdf)
    #print "No. of pages ",pdfReader.getNumPages()

    if(single=='2'):
        #if we want to split pages in custom range
        groups=rng.split(',') #this array contain every group of pages
        k=0
        for i in groups:
            if(len(i)==1): #to handle single pages
                i=i+'-'+i
            output = PdfFileWriter()
            for j in range(int(i[0])-1,int(i[2])): #to handle group of pages
                output.addPage(pdfReader.getPage(j))
            with open(os.path.join("splitted//%s.pdf") % (k + 1), "wb") as outputStream:
                output.write(outputStream)
            k+=1
        inputPdf.close()
        os.remove(path)
        shutil.make_archive(os.path.join("todownload//download"),'zip',os.path.join('splitted'))
        return True

    else:
        #if we split into single pages
        for i in range(pdfReader.numPages):
            output = PdfFileWriter()
            output.addPage(pdfReader.getPage(i))
            with open(os.path.join("splitted//%s.pdf") % (i+1), "wb") as outputStream:
                output.write(outputStream)
        inputPdf.close()
        os.remove(path)
        shutil.make_archive(os.path.join("todownload//download"),'zip',os.path.join('splitted'))
        return True

    return False


#--------------------------------------------------------------------------------
def function_merge(info,indexes):
    names=info[0]
    paths=info[1]
    #print(indexes)
    #print(names)
    #print(paths)
    shutil.rmtree('merged')
    os.mkdir('merged')
    merger = PdfFileMerger()
    for i in indexes:
        ind=int(i)-1
        merger.append(paths[ind])
    merger.write("merged//download.pdf")
    shutil.make_archive(os.path.join("todownload//download"), 'zip', os.path.join('merged'))
    return True