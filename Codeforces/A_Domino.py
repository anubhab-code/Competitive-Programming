n = int(input())
data = []
c1, c2 = 0, 0
flag = 0
for i in range(n):
    val = list(map(int, input().split()))
    data.append(tuple(val))
    c1 += val[0]
    c2 += val[1]
    if (c1 % 2) != (c2 % 2):
        flag = 1

if c1 % 2 == 1 and c2 % 2 == 1 and (c1+c2) % 2 == 0 and n > 1 and flag == 1:
    print(1)
elif c1 % 2 == 0 and c2 % 2 == 0:
    print(0)
else:
    print(-1)