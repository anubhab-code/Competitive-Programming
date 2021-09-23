from typing import Counter
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0
c1 = Counter(a)
c2 = Counter(b)
for i in range(1,6):
    if abs(c1[i]-c2[i]) % 2:
        print(-1)
        break
    ans += abs(c1[i]-c2[i])//2
else:
    if ans%2:
        print(-1)
    else:
        print(ans//2)