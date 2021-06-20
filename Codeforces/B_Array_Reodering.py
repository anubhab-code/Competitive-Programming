from math import gcd
for i in range(int(input())):
    ans=0
    n=int(input())
    l=list(map(int,input().split()))
    eve=[]
    odd=[]
    for a in range(len(l)):
        if l[a]%2!=0:
            odd.append(l[a])
        else:
            eve.append(l[a])
    final=eve+odd
    for j in range(0,n):
        for k in range(j+1,n):
            if gcd(2*final[k],final[j])>1:
                ans=ans+1
    print(ans)