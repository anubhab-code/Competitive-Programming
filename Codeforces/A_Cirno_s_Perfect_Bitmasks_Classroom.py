import math
for _ in range(int(input())):
    n = int(input())
    mask = 1
    if n==1:
        print(3)
        continue
    for i in range(32):
        if n&mask:
            index = i
            break
        mask<<=1
    x = int(math.log(n,2))
    if x==index:
        print(2**index+1)
    else:
        print(2**index)