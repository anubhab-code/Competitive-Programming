from math import floor,ceil
n=int(input())
flag=1
for _ in range(n):
    r=int(input())
    if r%2==0:
        print(r//2)
    else:
        if flag:
            print(ceil(r/2))
            flag=0
        else:
            print(floor(r/2))
            flag=1