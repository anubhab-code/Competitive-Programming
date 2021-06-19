convert=['A','D','F','G','X']

def adfgx_encrypt(plaintext, square):
    square=square.replace('j','i')
    ans=''
    for p in plaintext:
        if p=='j': 
            p='i'
        i=square.index(p)
        ans += convert[int(i/5)]+convert[i%5]
    return ans    
    
def adfgx_decrypt(c, square):
    ans=''
    for i in range(0,len(c),2):
        ans +=square[5*convert.index(c[i])+convert.index(c[i+1])]
    return ans
    