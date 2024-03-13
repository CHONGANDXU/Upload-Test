from docx2pdf import convert
import os

word_path = r"your word(.doc) file path"

word_to_pdf = r"your new pdf(.pdf) file path"

for i, j, name in os.walk(word_path):
    for word_name in name:
        convert(
            word_path + "/" + word_name,
            word_to_pdf + "/" + word_name.replace("docx", "pdf"),
        )
