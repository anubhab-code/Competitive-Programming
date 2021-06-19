def owl_pic(text):
    t = filter(lambda x: x in '8WTYUIOAHXVM', text.upper())
    return t + "''0v0''" + t[::-1]