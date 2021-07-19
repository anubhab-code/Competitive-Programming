from typing import Counter
for _ in range(int(input())):
    a,b,k = map(int,input().split())
    boys = list(map(int,input().split()))
    girls = list(map(int,input().split()))
    b = Counter(boys)
    g = Counter(girls)
    ans = 0
    for i in range(k):
        ans += k - (b[boys[i]] + g[girls[i]]) + 1
    print(ans//2)