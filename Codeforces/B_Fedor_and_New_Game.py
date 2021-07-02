l=[]
n,m,k=map(int,input().split())
for i in range(m+1):
    l.append(int(input()))
fed=l[-1]
l=l[:-1]
ans=0
for i in l:
    c=0
    p=fed
    a=True
    while(p and i):
        c+=((p^i)&1)
        if c>k:
            a=False
            break
        p=p>>1
        i=i>>1
    if p:
        while(p):
            c+=p&1
            p=p>>1
    else:
        while(i):
            c+=i&1
            i=i>>1
    if a and c<=k:
        ans+=1
print(ans)