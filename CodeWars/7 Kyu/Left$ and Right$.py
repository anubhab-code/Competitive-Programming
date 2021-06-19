def left(string,i=1):
    i=string.index(i) if type(i)==str else i
    return string[:i]
    
def right(string,i=1):
    i=string[::-1].index(i[::-1]) if type(i)==str else i
    return string[-i:] if i!=0 else ""