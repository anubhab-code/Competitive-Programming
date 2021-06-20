l = list(map(int, input().split()))
s = set(l)
ans = len(l)-len(s)
print(ans)