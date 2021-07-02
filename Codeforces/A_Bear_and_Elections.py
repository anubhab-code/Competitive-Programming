n=int(input())
l=list(map(int,input().split()))
ans=0
while True:
    ma=l[0]
    k=0
    for i in range(1,n):
        if l[i]>=ma:
            ma=l[i]
            k=i
    if k!=0 and ma>=l[0]:
        l[0]+=1
        l[k]-=1
        ans+=1
    else:
        break
print(ans)