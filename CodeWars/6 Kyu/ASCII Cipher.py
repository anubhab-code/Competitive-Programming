def ascii_cipher(message, key):
    pos_key = abs(key)
    i = 2
    while pos_key > 1:
        while pos_key % i == 0:
            pos_key //= i
        i += 1
    i -= 1
    if key < 0:
        i = -i
    return ''.join(chr((ord(c) + i) % 128) for c in message)