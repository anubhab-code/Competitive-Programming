for _ in range(int(input())):
    n,w = map(int,input().split())
    l = list(map(int,input().split()))
    ans = []
    for a,b in enumerate(l):
        ans.append([b,a+1])
    ans=sorted(ans)[::-1]
    c=0
    final = []
    for i in ans:
        if c+i[0] <= w:
            c += i[0]
            final.append(i[1])
    if c>=(w+1)//2:
        print(len(final))
        print(*final[::-1])
    else:
        print(-1)