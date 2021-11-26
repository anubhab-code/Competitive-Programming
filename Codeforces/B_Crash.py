n = int(input())
vis = set()
flag = 1
for i in range(n):
    x,k = map(int,input().split())
    if x == 0:
        vis.add((x,k))
    else:
        if (x-1,k) in vis:
            vis.add((x,k))
        else:
            flag = 0
if flag:
    print("YES")
else:
    print("NO")