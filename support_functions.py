import glob
import os
import PyPDF2


def read_pdf_from_pdf_direct(pdf_direct):
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
        origin.append(str(page_content.encode('ascii', 'ignore')))

    return origin


def read_save_textdata_from_pdf_folder(folder, save_folder):
    """

    :param folder: string
    :param save_folder: string
    :return: convert pdf to text file
    """
    data = []
    if os.path.exists(save_folder):
        for file in glob.glob(os.path.join(save_folder, '*.txt')):
            os.remove(file)

    for file in glob.glob(os.path.join(folder, '*.pdf')):
        data.append(read_pdf_from_pdf_direct(file))
        textfile_name = file.replace(folder, save_folder)
        textfile_name = textfile_name.replace('.pdf', '.txt')
        with open(textfile_name, mode='w') as save_file:
            for pdf_file in data[-1]:
                for page in pdf_file:
                    save_file.write(page)
    return data


def read_text_data(text_folder):
    """

    :param text_folder: string
    :return: list of strings
    """
    data = []
    for file in glob.glob(os.path.join(text_folder, '*.txt')):
        with open(file) as data_file:
            data.append(data_file.readline())
    return data


def calculate_compress_ratio(origin, compressed_data):
    """

    :param origin: string: non_encoded data
    :param compressed_data: list of encoded_data
    :return: compress_ratio
    """
    if len(origin) == 0:
        return 1.0
    origin_size = len(origin)
    # plus number of space when saving
    compressed_data_size = len(compressed_data)*2 - 1
    return origin_size / compressed_data_size


def calculate_real_compress_ratio_from_file(origin_folder, compressed_folder):
    """

    :param origin_folder: string
    :param compressed_folder: string
    :return: avg file compression ratio _ in real files
    """
    origin_files = glob.glob(os.path.join(origin_folder, '*.txt'))
    compressed_files = glob.glob(os.path.join(compressed_folder, '*.txt'))
    origin_size = 0
    compressed_size = 0

    for i in range(len(origin_files)):
        origin_size += os.path.getsize(origin_files[i])
        compressed_size += os.path.getsize(compressed_files[i])

    compression_ratio = origin_size/compressed_size

    return compression_ratio


def rename_all_file(prefix, folder_direct, extension):
    """

    :param folder_direct: string
    :return: rename all .pdf file in folder direct with format: origin_<number>.pdf
    """
    files = os.listdir(folder_direct)
    i = 1
    for file in files:
        os.rename(os.path.join(folder_direct, file), os.path.join(folder_direct, prefix + str(i) + extension))
        i = i + 1

def split_string(origin_string, n):
    return [origin_string[i:i + n] for i in range(0, len(origin_string), n)]

def save_text_file_into_folder(text_file_name, save_data, folder):
    """

    :param text_file_name: string
    :param save_data: list of string
    :param folder: string
    :return: text file is saved to folder
    """
    direct = os.path.join(folder, text_file_name)
    if os.path.exists(direct):
        os.remove(direct)

    with open(direct, 'w') as file:
        for element in save_data:
            file.write(str(element) + " ")