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
        a,b=vinp()
        aaa,bbb=a,b
        a=bin(a)[2:]
        b=bin(b)[2:]
        aa=len(a)
        bb=len(b)
        c=""
        if aa>bb:
            b="0"*(aa-bb) + b
        else:
            a="0"*abs(aa-bb) + a
        for i in range(max(aa,bb)):
            if a[i]==b[i]:
                c+=a[i]
            else:
                c+="0"
        c=int(c,2)
        pr((aaa^c)+(bbb^c))