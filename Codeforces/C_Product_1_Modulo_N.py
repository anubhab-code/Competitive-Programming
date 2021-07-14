import math
n = int(input())
ans = []
check = 1
for i in range(1,n):
    if math.gcd(i,n) == 1:
        ans.append(i)
        check = (i*check)%n
if check%n == 1:
    print(len(ans))
    print(*ans)
else:
    ans.pop()
    print(len(ans))
    print(*ans)