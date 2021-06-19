def center(str, width, fill=' '):
    return fill*((width+1-len(str))//2) + str + fill*((width-len(str))//2)