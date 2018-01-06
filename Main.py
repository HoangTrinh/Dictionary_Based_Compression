import LZW
import support_functions

# read data from pdf files
data = support_functions.read_data_from_folder('data')

sum_compression_ratio_of_data = 0

# list of files
for origins in data:

    print('\nstart a new file:')
    # list of pages per file
    for origin in origins:
        sum_compression_ratio_of_pdf_file = 0
        print('original data: ', origin)

        # compress + convenience purpose
        compressed_data,print_compress_data = LZW.encode(origin, take_list=True)

        print('compressed_data: ',  print_compress_data)

        # calculate compression ratio per page
        compression_ratio = support_functions.calculate_compress_ratio(origin, compressed_data)
        print('compression_ratio: %0.2f' % compression_ratio)

        # decompress
        decompressed_data = LZW.decode(compressed_data)

        # check result
        if origin == decompressed_data:
            print('decompressed_data equal original_data, Good job!')
            print('decompressed_data: ', decompressed_data)
            sum_compression_ratio_of_pdf_file += compression_ratio
        else:
            print('poor algorithm')

    sum_compression_ratio_of_data += (sum_compression_ratio_of_pdf_file / len(origins))

# average compression ratio for the whole data
avg_compress_ratio = sum_compression_ratio_of_data / len(data)
print('\naverage compression ratio: %0.2f' % avg_compress_ratio)
