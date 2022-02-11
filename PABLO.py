from PyPDF2 import PdfFileReader, PdfFileWriter
from math import *

path = "/my/absolute/path/myfile.pdf"

if __name__ == '__main__':
    pdf = PdfFileReader(path)
    pdf_writer = PdfFileWriter()
    
    MAX_PAGE = pdf.getNumPages()
    MAX_PART = ceil(MAX_PAGE / 32)
    
    page_index = -1
    count_part = 1

    while page_index != MAX_PAGE - 1:
        page_index += 1

        pdf_writer.addPage(pdf.getPage(page_index))
        
        if ((page_index + 1) % 32 == 0 and page_index != 0) or page_index == MAX_PAGE - 1:
            str_count_part = '0' + str(count_part) if count_part < 10 else str(count_part)

            print(f'Save {str_count_part}/{MAX_PART}')

            output = f'part_{str_count_part}.pdf'
            with open(output, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)
            
            pdf_writer = PdfFileWriter()
            count_part += 1
