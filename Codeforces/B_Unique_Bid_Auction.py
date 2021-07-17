from typing import Counter
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    c = Counter(l)
    ans = []
    k = list(c.keys())
    v = list(c.values())
    for i in range(len(v)):
        if v[i] == 1:
        	ans.append(k[i])
    if len(ans) == 0:
    	print(-1)
    else:	
    	print(l.index(min(ans))+1)