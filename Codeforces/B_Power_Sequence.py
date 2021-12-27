n = int(input())
l = list(map(int,input().split()))
l = sorted(l)
mx = 100*(10**9)+9
i = 1
ans = float('inf')
while i**(n-1)<mx:
    p=0
    for j in range(n):
        p+=abs(l[j]-i**j)
    i+=1
    ans=min(ans,p)
print(ans)