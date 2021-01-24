# sample commmand-line instruction
# ensure that you install PyPDF2 with pip install PyPDF2
# python trimpdf.py <your_PDF_file_name> 0-0 5-9 13-13 23-28 29-29

import sys
import PyPDF2

# Collect the arguments
file_name = sys.argv[1]
pages_range = sys.argv[2:]
new_file_name = 'PDF_Trimmed.pdf'


# looping through the pages_range
with open(file_name, 'rb') as file:
    writer = PyPDF2.PdfFileWriter()
    reader = PyPDF2.PdfFileReader(file)
    all_pages = []
    for x in pages_range:
        temp_list = x.split('-',1)
        diff = int(temp_list[1]) - int(temp_list[0])
        temp_list2 = []
        for y in range(int(temp_list[0]),int(temp_list[0])+diff+1,1):
            temp_list2.append(y)
        all_pages.extend(temp_list2)
    for i in all_pages:
        page = reader.getPage(i)
        writer.addPage(page)
    with open(new_file_name, 'wb') as new_file:
        writer.write(new_file)
        print(f'Your PDF is trimmed successfully. All the required pages are in file {new_file_name}')




