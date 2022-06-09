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
        c[l[i]]=c.get(l[i],[])+[i]
    return c
if __name__ =="__main__":
    cou=inp()
    for _ in range(cou):
        s,s1 = sinp(3)
        n,m = len(s),len(s1)
        c = indc(s,n)
        c1 = Counter(s)
        c2 = Counter(s1)
        l3 = []
        p = True
        for i in c2.keys():
            if c.get(i,[])!=[] and c1[i]>=c2[i]:
                l3+=c[i][-c2[i]:]
            else:
                p = False
                break
        if p:
            l3.sort()
            z = 0
            # pr(l3)
            for i in l3:
                # pr(s[i],s1[z])
                if s[i]!=s1[z]:
                    p = False
                    pr("NO")
                    break
                z+=1
            if p:
                pr("YES")
        else:
            pr("NO")