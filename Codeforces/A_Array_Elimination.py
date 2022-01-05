import math
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    bits=[]
    g=0
    for i in range(31):
        c=0
        for j in l:
            if((j&(1<<i))):
                c+=1
        bits.append(c)
        g=math.gcd(g,c)
    if g==0:
        for i in range(n):
            print(i+1,end=' ')
    else:
        ans=[]
        for i in range(1,g+1):
            if i*i>g:
                break
            if g%i==0:
                ans.append(i)
                ans.append(g//i)
        ans=list(set(ans))
        ans=sorted(ans)
        print(*ans)