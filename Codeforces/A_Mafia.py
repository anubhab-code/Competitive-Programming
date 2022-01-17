from math import ceil
n = int(input())
l = list(map(int,input().split()))
ans = ceil(sum(l)/(n-1))
if ans<max(l):
    ans = max(l)
print(ans)