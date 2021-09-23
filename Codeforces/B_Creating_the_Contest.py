n=int(input())
a=list(map(int,input().split()))
ans=1
temp=1
for i in range(n-1):
    if 2*a[i]>=a[i+1]:
        temp+=1
        ans=max(ans,temp)
    else:
        temp=1
print(ans)