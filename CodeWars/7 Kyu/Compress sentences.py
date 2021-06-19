def compress(sentence):
    d={}
    i=0
    r=''
    for w in sentence.lower().split():
        if w not in d:
            d[w]=i
            i+=1
        r+=str(d[w])
    return r