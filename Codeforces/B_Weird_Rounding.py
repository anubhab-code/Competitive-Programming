n,k=map(int,input().split())
ans=0
c0=0
n=str(n)
i=len(n)-1
while c0!=k and i>=0:
    if c0==k:
        break
    if n[i]=="0":
        c0+=1
    else:
        ans+=1
    i-=1
if c0!=k:
    print(len(n)-1)
else:
    print(ans)