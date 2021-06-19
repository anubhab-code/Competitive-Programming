def scale(strng, k, n):
    words = strng.split()
    words_h = ("".join(char * k for char in word) for word in words) 
    return "\n".join("\n".join(word for _ in range(n)) for word in words_h)