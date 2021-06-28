n,k = map(int,input().split())
l = list(map(int,input().split()))
check = [k]*n
ans = 0
while l!=check:
    new = []
    for i in range(n):
        if (l[i] < k) and (l[i] not in new):
            new.append(l[i])
            l[i] += 1
    ans += 1
    new=[]
print(ans)