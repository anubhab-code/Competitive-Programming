#     __  __                __    _ __      ______                
#    / / / /___ ___________/ /_  (_) /_    / ____/___ __________ _
#   / /_/ / __ `/ ___/ ___/ __ \/ / __/   / / __/ __ `/ ___/ __ `/
#  / __  / /_/ / /  (__  ) / / / / /_    / /_/ / /_/ / /  / /_/ / 
# /_/ /_/\__,_/_/  /____/_/ /_/_/\__/____\____/\__,_/_/   \__, /  
#                                  /_____/               /____/   
 
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
        n = inp()
        a = linp()
        b = linp()
        s = set()
        p = True
        temp = 0
        for i in range(n):
            if b[i]==0:
                temp = max(temp,a[i])
        for i in range(n):
            if b[i]!=0:
                t = a[i]-b[i]
                if t>=0:
                    s.add(t)
                    if len(s)>1:
                        pr("NO")
                        p = False
                        break
                else:
                    pr("NO")
                    p = False
                    break
        if p:
            if len(s)==0:
                pr("YES")
            else:
                if temp<=list(s)[0]:
                    pr("YES")
                else:
                    pr("NO")