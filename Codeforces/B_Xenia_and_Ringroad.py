n,m = map(int,input().split())
l = list(map(int,input().split()))
g=1
ans=0
for i in l:
    if g<=i:
        ans+=i-g
        g=i
    else:
        ans+=(n-g)+i
        g=i
print(ans)