def split_and_merge(string, sp):
    # your code here
    words = string.split(' ')
    l =[]
    for i in words:
        i = sp.join(i)
        l.append(i)
    return ' '.join(l)