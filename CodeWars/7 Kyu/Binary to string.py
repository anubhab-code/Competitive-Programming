def binary_to_string(binary):
    a = binary.split("0b")
    return "".join([chr(int(b,2)) for b in a if b])