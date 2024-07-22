def binary_to_text(binary_code):
    binary_code = binary_code.replace(" ", "")
    try:
        text = ''.join(chr(int(binary_code[i:i+8], 2)) for i in range(0, len(binary_code), 8))
    except ValueError:
        text = "Invalid binary code"
    return text
