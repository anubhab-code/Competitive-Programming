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
    n,k = linp()
    l = linp()
    c = Counter(l)
    t = max(c.values())
    lis = [i+1 for i in range(k)]
    if t>k:
        pr("NO")
    else:
        pr("YES")
        csort(c)
        curr = 0
        d = dd(list)
        for i in c.keys():
            temp = c[i]
            end = curr+temp
            if end>k:
                d[i] = lis[curr:k] + lis[0:end-k]
                curr = end-k
            else:
                d[i] = lis[curr:end]
                curr = end
        for i in range(n):
            pr(d[l[i]][0],end=" ")
            d[l[i]] = d[l[i]][1:]
        pr()
