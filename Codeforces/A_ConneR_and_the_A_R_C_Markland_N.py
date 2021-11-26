from collections import Counter
from sys import *
from collections import defaultdict as dd
from math import *
 
# sys.stdin = open('input.txt', 'r')  
# sys.stdout = open('output.txt', 'w')
 
#input functions
def inp():
    return int(stdin.readline().strip())
def vinp():
    return map(int,stdin.readline().strip().split())
def linp():
    return list(map(int,stdin.readline().strip().split()))
def sinp(n = 1):
    if n==1:
        return stdin.readline().strip()
    elif n==2:
        return list(stdin.readline().strip())
    else:
        return list(stdin.readline().split())
 
#output function
def pr(*x, end = "\n"):
    print(*x,end = end)
 
#others
def mod(f, val = 1000000007):
    return f % val
def csort(c):
    sorted(c.items(), key=lambda pair: pair[1], reverse=True)
def indc(l,n):
    c={}
    for i in range(n):
        c[l[i]]=c.get(l[i],[])+[i+1]
    return c
 
if __name__ =="__main__":
    cou=inp()
    for _ in range(cou):
        a,b,c = vinp()
        l = linp()
        m,m2 = 0,0
        m1f,m2f = False,False
        c = Counter(l)
        for i in range(b,a+1):
            if c.get(i,0) == 0:
                m = i
                m1f = True
                break
        for i in range(b-1,max(1,b-1000)-1,-1):
            if c.get(i,0) == 0:
                m2 = i
                m2f = True
                break
        # pr(m,m2)
        if m1f and m2f:
            pr(min(m-b,b-m2))
        elif m1f:
            pr(m-b)
        else:
            pr(b-m2)