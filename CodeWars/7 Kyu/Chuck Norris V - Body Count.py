good = 'A8A8A8A8A8.-A%8.88.'
def g(x):
    for i in range(len(good)):
        if good[i]=="A" and not x[i].isupper(): return False
        elif good[i]=="8" and not x[i].isdigit(): return False
        elif good[i] in '%-.' and good[i]!=x[i]: return False
    return True
    
def body_count(code):
    return any(g(code[i:i+19]) for i in range(len(code)-18))