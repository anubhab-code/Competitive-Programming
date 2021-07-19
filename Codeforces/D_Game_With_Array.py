n,s = map(int,input().split())
if 2*n<=s:
    ans = [2]*(n-1)
    ans.append(s - 2*n + 2)
    print("YES")
    print(*ans)
    print(1)
else:
    print("NO")