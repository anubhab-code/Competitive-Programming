def encryption(string):
    return ' '.join([CHAR_TO_MORSE.get(c, c) for c in string])