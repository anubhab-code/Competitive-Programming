d=int(input())
n=int(input())
l=list(map(int,input().split()))
ans=0
for i in range(n-1):
    ans+=d-l[i]
print(ans)