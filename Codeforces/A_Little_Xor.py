n=int(input());
ans=0
l=list(map(int,input().split()))
for i in range(n):
    x=0
    for j in range(i,n):
        x=x^l[j]
        ans=max(ans,x)
print(ans)