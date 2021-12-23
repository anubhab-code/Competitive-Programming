from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    ans = defaultdict(int)
    j = 1
    while j**2<=n:
        ans[j**2]+=1
        j+=1
    i = 1
    while i**3<=n:
        ans[i**3]+=1
        i+=1
    print(len(ans))