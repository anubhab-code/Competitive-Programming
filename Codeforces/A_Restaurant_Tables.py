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
    c,a,b = vinp()
    z=0
    l = linp()
    f=0
    for i in l:
        if i==1:
            if a>0:
                a-=1
            elif b>0:
                b-=1
                z+=1
            elif z>0:
                z-=1
            else:
                f+=1
        else:
            if b>0:
                b-=1
            else:
                f+=2
    pr(f)