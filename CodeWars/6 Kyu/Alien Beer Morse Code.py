def morse_converter(string):
    s=0
    for i in range(0,len(string),5):
        n=string[i:i+5]
        a=len(n.rstrip('-'))
        if a==5:a+=len(n.rstrip('.'))
        s*=10
        s+=a
    return s