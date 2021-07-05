n = int(input())
l = list(map(int, input().split()))
ans = []
l = sorted(l)
ans = [l[-1]] + l[1:(n-1)] + [l[0]]
print(*ans)