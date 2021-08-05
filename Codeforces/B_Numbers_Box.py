from typing import Counter
import sys
from collections import defaultdict as dd
from math import *
 
def vinp():
    return map(int,input().split())
def linp():
    return list(map(int,input().split()))
def sinp():
    return input()
def inp():
    return int(input())
def mod(f):
    return f % 1000000007
def pr(*x):
    print(*x)
def finp():
    f=open("input.txt","r")
    f=f.read().split("\n")
    return f
def finp():
    f=open("input.txt","r")
    f=f.read().split("\n")
    return f
def fout():
    return open("output.txt","w")
def fpr(f,x):
    f.write(x+"\n")
def csort(c):
    sorted(c.items(), key=lambda pair: pair[1], reverse=True)
def indc(l,n):
    c={}
    for i in range(n):
        c[l[i]]=c.get(l[i],[])+[i+1]
    return c
 
if __name__ =="__main__":
    cou=inp()
    for i in range(cou):
        n,m=vinp()
        l=[linp() for i in range(n)]
        s=0
        c=0
        mx=sys.maxsize
        for i in range(n):
            for j in range(m):
                if l[i][j]<0:
                    c+=1
                s+=abs(l[i][j])
                if abs(l[i][j])<mx:
                    mx=abs(l[i][j])
        if c%2!=0:
            pr(s-2*mx)
        else:
            pr(s)