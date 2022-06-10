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
    n = inp()
    s = sinp()
    z,o,t = [],[],[]
    zc,oc,tc = 0,0,0
    for i in range(n):
        if s[i]=="0":
            z.append(i+1)
            zc+=1
        elif s[i]=="1":
            o.append(i+1)
            oc+=1
        else:
            t.append(i+1)
            tc+=1
    f = n//3
    ze,oe,te = max(0,zc-f),max(0,oc-f),max(0,tc-f)
    zn,on,tn = max(0,f-zc),max(0,f-oc),max(0,f-tc)
    # pr(ze,oe,te,zn,on,tn)
    ztoo = min(ze,on)
    ze-=ztoo
    on-=ztoo
    ztot = min(ze,tn)
    ze-=ztot
    tn-=ztot
    if ztot:
        t += z[-ztot:]
        z = z[:-ztot]
    if ztoo:
        o += z[-ztoo:]
        z = z[:-ztoo]
    otoz = min(oe,zn)
    oe-=otoz
    zn-=otoz
    if otoz:
        z += o[:otoz]
        o = o[otoz:]
    otot = min(oe,tn)
    oe-=otot
    tn-=otot
    if otot:
        t+=o[-otot:]
        o=o[:-otot] 
    ttoz = min(te,zn)
    te-=ttoz
    zn-=ttoz
    if ttoz:
        z += t[:ttoz]
        t = t[ttoz:]
    ttoo = min(te,on)
    te-=ttoo
    on-=ttoo
    if ttoo:
        o+=t[:ttoo]
        t=t[ttoo:] 
    ans = ["" for i in range(n)]
    for i in z:
        ans[i-1]="0"
    for i in o:
        ans[i-1]="1"
    for i in t:
        ans[i-1]="2"
    pr("".join(ans))