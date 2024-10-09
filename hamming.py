# hamming.py

def calculate_parity_bits(m):
    """Calculate number of parity bits required for m data bits."""
    for i in range(m):
        if (2**i >= m + i + 1):
            return i

def generate_hamming_code(data):
    """Generate Hamming code for the given binary data string."""
    data = list(data)
    m = len(data)
    r = calculate_parity_bits(m)
    total_length = m + r

    hamming_code = ['0'] * total_length
    j = 0  # Pointer for data bits
    for i in range(1, total_length + 1):
        if (i & (i - 1)) == 0:  # Parity bit positions are powers of 2
            continue
        hamming_code[i - 1] = data[j]
        j += 1

    # Set parity bits
    for i in range(r):
        parity_pos = 2**i - 1
        parity_value = 0
        for j in range(parity_pos, total_length, 2**(i + 1)):
            parity_value ^= sum(int(bit) for bit in hamming_code[j:j + 2**i])
        hamming_code[parity_pos] = str(parity_value % 2)

    return ''.join(hamming_code)

def detect_and_correct_error(hamming_code):
    """Detect and correct a single-bit error in the Hamming code."""
    total_length = len(hamming_code)
    r = calculate_parity_bits(total_length - calculate_parity_bits(total_length))
    error_position = 0

    for i in range(r):
        parity_pos = 2**i - 1
        parity_value = 0
        for j in range(parity_pos, total_length, 2**(i + 1)):
            parity_value ^= sum(int(bit) for bit in hamming_code[j:j + 2**i])
        if parity_value % 2 != 0:
            error_position += 2**i

    if error_position == 0:
        return hamming_code, False  # No error
    else:
        corrected_code = list(hamming_code)
        corrected_code[error_position - 1] = '1' if corrected_code[error_position - 1] == '0' else '0'
        return ''.join(corrected_code), True  # Error corrected
