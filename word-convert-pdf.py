from docx2pdf import convert
import os
import time

word_path = r'/Users/chengchong/Desktop/OneDrive\ -\ yc3sq/docx'

word_to_pdf = r'/Users/chengchong/Desktop/OneDrive\ -\ yc3sq/docx'

for i,j,name in os.walk(word_path):
    for word_name in name:
         convert(word_path+"/"+word_name, word_to_pdf+"/"+word_name.replace("docx","pdf"))
