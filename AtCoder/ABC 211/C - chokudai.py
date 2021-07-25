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
    s=sinp()
    fi="chokudai"
    m=len(s)
    dp = [[0] * (9) for i in range(m + 1)]
    for i in range(9):
        dp[0][i]=0
    for i in range(m+1):
        dp[i][0]=1
    for i in range(1,m+1):
        for j in range(1,9):
            if s[i-1]==fi[j-1]:
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    pr(mod(dp[m][8]))