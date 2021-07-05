n,k = map(int,input().split())
l = list(map(int,input().split()))
ans=0
j=0

for i in range(n):
    while l[i]-l[j]>k:
        j+=1
    total=i-j
    ans+=total*(total-1)//2
print(ans)