import os
from pdf2docx import Converter

# Obtain all the pdf file in the current directory
pdf_files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.pdf')]

# Traverse all the pdf file in the path
for pdf_file in pdf_files:
    # Name of output file
    docx_file = pdf_file.rsplit('.', 1)[0] + '.docx'

    # The file to be converted
    print(f"Is now converting: {pdf_file} into {docx_file}")

    # 進行轉換
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()

print("Complete!!!。")