def each_char(string, arg):
    try:
        return ''.join(char + arg for char in string)
    except TypeError:
        return ''.join(arg(char) for char in string)