from typing import Counter
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    d = {}
    di = Counter(l)
    ma = max(di.values())
    c=0 
    for i in di.values():
        if i==ma:
            c+=1
    left = n-(c*ma)
    fill = left//(ma-1)
    print(c+fill-1)