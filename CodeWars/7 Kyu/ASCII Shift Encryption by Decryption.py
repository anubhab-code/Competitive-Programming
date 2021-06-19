def ascii_encrypt(pt):
    r=""
    for i in range(len(pt)): r+=chr(ord(pt[i])+i)
    return r
    
def ascii_decrypt(pt):
    r=""
    for i in range(len(pt)): r+=chr(ord(pt[i])-i)
    return r