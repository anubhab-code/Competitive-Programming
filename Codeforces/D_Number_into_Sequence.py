from math import *
for _ in range(int(input())):
    n = int(input())
    i=1
    j=1
    copy=n
    ans=[]
    for k in range(2,int(sqrt(n))+2):
        c=0
        while n%k==0:
            n//=k
            c+=1
        if c>i:
            i=c
            j=k
    for k in range(i-1):
        ans.append(j)
        copy//=j
    ans.append(copy)
    print(i)
    print(*ans)