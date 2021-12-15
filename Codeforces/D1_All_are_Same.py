from math import gcd
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    mi=min(l)
    temp=[]
    for i in l:
        if i-mi!=0:
            temp.append(i-mi)
    if len(temp)==0:
        print(-1)
    elif len(temp)==1:
        print(temp[0])
    else:
        ans = gcd(temp[1],temp[0])
        for i in range(2, len(temp)):
            ans = gcd(ans, temp[i])
        print(ans)
