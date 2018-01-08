import PyPDF2
import sys
import os
import glob

def read_pdf_from_direct(pdf_direct):
    """

    :param pdf_direct: string
    :return: list of text_encoded for all page(s) of pdf_direct file
    """
    print(pdf_direct)
    origin = []
    pdf_file = open(pdf_direct, 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    for page_index in range(number_of_pages):
        page = read_pdf.getPage(page_index)
        page_content = page.extractText()
        origin.append(str(page_content.encode('ascii','ignore')))

    return origin

def read_data_from_folder(folder):
    """

    :param folder: string: data_folder
    :return: list ( file ) of lists ( page ) ( b/c pdf file may contain more than 1 page )
    """

    data = []
    for file in glob.glob(os.path.join(folder, '*.pdf')):
        data.append(read_pdf_from_direct(file))

    return data

def calculate_compress_ratio(origin, compressed_data):
    """

    :param origin: string: non_encoded data
    :param compressed_data: list of encoded_data
    :return: compress_ratio
    """

    origin_size = sys.getsizeof(origin)
    compressed_data_size = sys.getsizeof(compressed_data)
    return origin_size/compressed_data_size

def rename_all_file(folder_direct):
    files = os.listdir(folder_direct)
    i = 1
    for file in files:
        os.rename(os.path.join(folder_direct, file), os.path.join(folder_direct,'origin_' + str(i) + '.pdf'))
        i = i + 1
#rename_all_file('data')