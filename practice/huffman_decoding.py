def huffman_decode(input_data):

    num_chars, _ = map(int, input_data[0].split())
    codes = {}
    for line in input_data[1:num_chars + 1]:
        char, code = line.split(": ")
        codes[code] = char.strip("'")
    encoded_text = input_data[-1]

    decoded_text = ""
    current_code = ""
    for bit in encoded_text:
        current_code += bit
        if current_code in codes:
            decoded_text += codes[current_code]
            current_code = ""

    print(decoded_text)

input_data = [
    "12 60",
    "' ': 1011",
    "'.': 1110",
    "'D': 1000",
    "'c': 000",
    "'d': 001",
    "'e': 1001",
    "'i': 010",
    "'m': 1100",
    "'n': 1010",
    "'o': 1111",
    "'s': 011",
    "'u': 1101",
    "100011110001001101000111111011001010011000010110011010111110"
]

huffman_decode(input_data)