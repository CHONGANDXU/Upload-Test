from win32com.client import Dispatch
from os import walk
import os
import time

wdFormatPDF = 17

def doc2pdf(input_file):
    word = Dispatch('Word.Application')
    doc = word.Documents.Open(input_file)
    print(input_file)
    doc.SaveAs(input_file.replace(".docx", ".pdf"), FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()


if __name__ == "__main__":
    doc_files = []
    directory = "C:"
    for root, dirs, filenames in walk(directory):
        for file in filenames:
            if file.endswith(".doc") or file.endswith(".docx"):
                print(os.path.abspath(root + "\\" + file))
                print(os.path.abspath(root + "\\" + file).replace(".docx",".pdf"))
                doc2pdf(os.path.abspath(root + "\\" + file))
            else:
                continue
            time.sleep(3)
