n=int(input())
l=list(map(int,input().split()))
ans=[0]*n
minn=0
maxx=10**19
for i in range(n//2):
    ans[i]=max(minn,l[i]-maxx)
    ans[n-i-1]=l[i]-ans[i]
    minn=ans[i]
    maxx=ans[n-i-1]
print(*ans)