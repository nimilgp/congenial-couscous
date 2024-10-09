# lzw.py

def lzw_compress(uncompressed):
    """Compress a string using LZW algorithm."""
    # Build the dictionary.
    dictionary = {chr(i): i for i in range(256)}
    dict_size = 256
    w = ""
    compressed_data = []

    # LZW Compression
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            compressed_data.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # Output the code for w.
    if w:
        compressed_data.append(dictionary[w])

    return compressed_data

def lzw_decompress(compressed):
    """Decompress a list of output ks to a string."""
    # Build the dictionary.
    dictionary = {i: chr(i) for i in range(256)}
    dict_size = 256
    w = chr(compressed.pop(0))
    decompressed_data = w

    # LZW Decompression
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError("Bad compressed k: {}".format(k))
        decompressed_data += entry

        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry

    return decompressed_data
