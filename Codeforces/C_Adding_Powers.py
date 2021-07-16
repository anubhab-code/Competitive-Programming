from math import log
from collections import defaultdict
def convbase(num,base):
    if num == 0:
        x = 1 
    else:
        for i in range(55):
            if base**i >= num:
                x = i + 1 
                break
    ans = []
    for i in range(x-1,-1,-1):
        p = num//(base**i)
        num = num%(base**i)
        ans.append(str(p))
    return ans

for _ in range(int(input())):
    n,k = map(int,input().split(' '))
    arr = [int(w) for w in input().split(' ')]
    res = []
    for item in arr:
        p = convbase(item,k)
        res.append(p)
    l = 0 
    ans = 'YES'
    for item in res:
        l = max(l,len(item))
    for i in range(n):
        res[i] = ['0']*(l-len(res[i])) + res[i]
    for i in range(l):
        d = defaultdict(int)
        count = 0 
        for j in range(len(res)):
            count  = count + int(res[j][i])
        if count>1:
            ans = 'NO'
            break
    print(ans)