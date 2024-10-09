# crc.py

def xor(a, b):
    """Perform bitwise XOR between two binary strings."""
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend, divisor):
    """Performs Modulo-2 division (CRC division)."""
    pick = len(divisor)
    tmp = dividend[0:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0' * pick, tmp) + dividend[pick]
        pick += 1

    # For the last iteration
    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    return tmp

def encode_data(data, key):
    """Encode data using CRC by appending checksum."""
    keylen = len(key)
    appended_data = data + '0' * (keylen - 1)
    remainder = mod2div(appended_data, key)
    return data + remainder

def verify_data(data, key):
    """Verify data by recalculating CRC and checking if remainder is zero."""
    remainder = mod2div(data, key)
    return remainder == '0' * (len(key) - 1)
