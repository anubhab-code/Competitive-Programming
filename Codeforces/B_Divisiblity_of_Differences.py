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
    a,b,c = vinp()
    k = linp()
    l = [0 for i in range(c)]
    l2 = [[] for i in range(c)]
    p = True
    for i in range(a):
        n = k[i]%c
        l[n-1]+=1
        l2[n-1].append(i)
    for i in range(c):
        if l[i]>=b:
            pr("Yes")
            p =False
            for j in range(b):
                pr(k[l2[i][j]],end=" ")
            break
    if p:
        pr("No")
    else:
        pr()