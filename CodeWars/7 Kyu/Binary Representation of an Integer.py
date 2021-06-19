def showBits(n):
    l=[]
    for i in range (32):
          r=n%2
          l.append(r)
          n //=2
    l.reverse()
    return l
          