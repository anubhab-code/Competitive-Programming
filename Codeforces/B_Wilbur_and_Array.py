n=int(input())
l=list(map(int,input().split()))
ans=0
for i in range(1,n):
    ans+=abs(l[i]-l[i-1])
print(ans+abs(l[0]))