n,m = map(int,input().split())
l = list(map(int,input().split()))
l=sorted(l)
j = n-1
i=0
ans=0
while i <= j:
    if l[i] + l[j] > m:
        j-=1
    else:
        i+=1
        j-=1
    ans+=1
print(ans)