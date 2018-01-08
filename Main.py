import LZW
import support_functions

# read data from pdf files
data = support_functions.read_data_from_folder('data')

sum_compression_ratio_of_data = 0

# list of files
for pdf_file in data:
    print('\nstart a new file:')
    sum_compression_ratio_of_pdf_file = 0

    # list of pages per file
    for page in pdf_file:
        print('original data: ', page)

        # compress + convenience purpose
        compress_data = LZW.encode(page)
        print('compressed_data: ', compress_data)

        # decompress
        decompressed_data = LZW.decode(compress_data)

        # check result
        if page == decompressed_data:
            print('decompressed_data equal original_data, Good job!')

        else:
            exit(404, 'POOR Algorithm')

        print('decompressed_data: ', decompressed_data)

        # calculate compression ratio per page
        compression_ratio = support_functions.calculate_compress_ratio(page, compress_data)
        print('compression_ratio: %0.2f' % compression_ratio)
        sum_compression_ratio_of_pdf_file += compression_ratio

    sum_compression_ratio_of_data += (sum_compression_ratio_of_pdf_file / len(pdf_file))

# average compression ratio for the whole data
avg_compress_ratio = sum_compression_ratio_of_data / len(data)
print('\naverage compression ratio: %0.2f' % avg_compress_ratio)
