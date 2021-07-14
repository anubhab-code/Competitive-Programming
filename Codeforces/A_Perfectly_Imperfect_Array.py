import math
for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    flag = 0
    for i in l:
        if int(math.sqrt(i))**2!=i:
            flag=1
            break
    if flag==1:
        print('YES')
    else:
        print('NO')