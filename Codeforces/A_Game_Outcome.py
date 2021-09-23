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
    l=[]
    s=[]
    for i in range(cou):
        l.append(linp())
        s.append(sum(l[-1]))
    s2=[0 for i in range(cou)]
    for i in range(cou):
        for j in range(cou):
            s2[i]+=l[j][i]
    k=0
    # pr(s)
    # pr(s2)
    for i in s2:
        for j in s:
            if i>j:
                k+=1
    pr(k)