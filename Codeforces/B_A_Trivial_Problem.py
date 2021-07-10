m = int(input())
c = 0
i = n = 5
ans = []
while c<=m:
    while n%5==0:
        c += 1
        n //= 5
    if c==m:
        ans.append(i)
    i += 1
    n = i
if ans==[]:
    print(0)
else:
    print(5)
    print(*ans)