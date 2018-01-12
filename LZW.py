def encode(origin):
    """

    :param origin: string
    :param take_list: Boolean
    :return: output 2 type ( integer generator, list of integer) if take_list = True else output integer generator
    """
    # create dictionary with 256 ASCII code
    dictionary_size = 256
    dictionary = {chr(i): i for i in range(dictionary_size)}

    s = ''
    compressed_data = []

    for character in origin:
        sc = s + character
        if sc in dictionary:
            s = sc
        else:
            compressed_data.append(dictionary[s])
            dictionary[sc] = dictionary_size
            dictionary_size += 1
            s = character
    if s:
        compressed_data.append(dictionary[s])

    return compressed_data


def decode(compressed_data):
    """

    :param compressed_data: integer list
    :return: decompresed_data
    """

    # create inverted dictionary with 256 ASCII code
    dictionary_size = 256
    dictionary = {i: chr(i) for i in range(dictionary_size)}

    s = decompressed_data = ''

    for number in compressed_data:
        if number in dictionary:
            entry = dictionary[number]

        else:
            entry = s + s[0]
        decompressed_data += entry

        if s != '':
            dictionary[dictionary_size] = s + entry[0]
            dictionary_size += 1
        s = entry

    # make sure output as string
    decompressed_data = ''.join(str(e) for e in decompressed_data)
    return decompressed_data
