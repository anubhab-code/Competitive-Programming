from collections import Counter
n = int(input())
data = list(map(int,input().split()))
a=0
for i in range(n):
    data[i]=data[i]%200
c=Counter(data)
for i,j in c.items():
    z=((j-1)*(j))//2
    if j>=2:
        if z:
            a+=z
        else:
            a+=2
print(a)