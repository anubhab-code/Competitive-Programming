n,m,k = map(int,input().split())
d = list(map(int,input().split()))
m = list(map(int,input().split()))
ans = []
check = 10**18
for i in range(len(d)):
    frog=d[i]
    c=0
    for j in range(len(m)):
        if m[j]%frog==0:
            c+=1
    if c<check:
        ans.clear()
        ans.append(i+1)
        check=c
    elif c==check:
        ans.append(i+1)
        c=check
print(len(ans))
print(*ans)