def encode(origin, take_list = False ):
    """

    :param origin: string
    :param take_list: Boolean
    :return: output 2 type ( integer generator, list of integer) if take_list = True else output integer generator
    """
    #create dictionary with 256 ASCII code
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

    # make sure output as separated integer ( list is wasted type of storage in this case )
    if take_list:
        list_compressed_data = compressed_data
        compressed_data = (int(element) for element in compressed_data)
        return compressed_data, list_compressed_data
    else:
        compressed_data = (int(element) for element in compressed_data)


    return compressed_data



def decode(compressed_data):
    """

    :param compressed_data: have to be a list because of prefix problem
    :return:
    """

    # create inverted dictionary with 256 ASCII code
    dictionary_size = 256
    dictionary = {i: chr(i) for i in range(dictionary_size)}

    s = origin = ''

    for number in compressed_data:
        if number in dictionary:
            entry = dictionary[number]

        #elif number == dictionary_size:
        else:
            entry = s + s[0]
        origin += entry

        if s != '':
            dictionary[dictionary_size] = s + entry[0]
            dictionary_size +=1
        s = entry

    # make sure output as string
    origin = ''.join(str(e) for e in origin)
    return origin

