from collections import Counter
l = set()
for i in range(100):
    for j in range(100):
        for k in range(100):
            if (i+j+k)%10 == 3:
                l.add(tuple(sorted((i%10, j%10, k%10))))
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(lambda x: int(x) % 10, input().split()))
    c = Counter(a)
    flag=0
    for i,j,k in l:
        d = Counter([i,j,k])
        for k,v in d.items():
            if c[k] < v:
                break
        else:
            flag=1
            break
    if flag:
        print("YES")
    else:
        print("NO")