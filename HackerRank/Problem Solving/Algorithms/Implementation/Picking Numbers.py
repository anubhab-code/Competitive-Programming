import sys

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
d = {x:0 for x in range(1,100)}

for i in a:
    d[i] = d.get(i,0)+1

maxi = 0
arr = list(d.keys())
for i in range(1,99):
    maxi = max(maxi,d[i]+d[i+1])
print(maxi)