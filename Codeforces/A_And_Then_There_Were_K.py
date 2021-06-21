import math
for _ in range(int(input())):
    n=int(input())
    ans=(2**int(math.log(n,2))) - 1
    print(ans)