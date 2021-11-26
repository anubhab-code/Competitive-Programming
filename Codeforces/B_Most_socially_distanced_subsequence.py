for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    ans = [l[0]]
    for i in range(1,n-1):
        if (l[i-1]>l[i] and l[i]<l[i+1]) or (l[i-1]<l[i] and l[i]>l[i+1]):
            ans.append(l[i])
    ans.append(l[-1])
    print(len(ans))
    print(*ans)