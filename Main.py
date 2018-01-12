import LZW
import support_functions

# Run 1 time
#support_functions.read_save_textdata_from_pdf_folder('pdf_data', 'text_data')

# Read data from text
data = support_functions.read_text_data('text_data')

compression_ratio_of_data = 0
i = 1
# list of files
for pdf_file in data:
    print('\nstart a new file:')

    print('original data: ', pdf_file)

    # compress + convenience purpose
    compress_data = LZW.encode(pdf_file)
    print('compressed_data: ', compress_data)

    # decompress
    decompressed_data = LZW.decode(compress_data)

    # check result
    if pdf_file == decompressed_data:
        print('decompressed_data equal original_data, Good job!')

    else:
        exit(404, 'POOR Algorithm')

    print('decompressed_data: ', decompressed_data)

    # calculate compression ratio per page
    compression_ratio = support_functions.calculate_compress_ratio(pdf_file, compress_data)
    print('compression_ratio: %0.2f' % compression_ratio)
    compression_ratio_of_data += compression_ratio

    # save compressed data
    support_functions.save_text_file_into_folder('compressed_' + str(i) + '.txt', compress_data, 'compressed_data' )
    i += 1

# average compression ratio for the whole data
compression_ratio_of_data /= len(data)
print('\naverage compression ratio: %0.2f' % compression_ratio_of_data)
real_compression_ratio = support_functions.calculate_real_compress_ratio_from_file('text_data', 'compressed_data')
print('\nreal compression ratio: %0.2f' % real_compression_ratio)

with open('record.txt', 'w') as result:
    result.write('Theory: ' + str(compression_ratio) + ' Real: ' + str(real_compression_ratio))