from math import *
n = int(input())
a = list(map(int,input().split()))
for i in range(n):
    for j in range(i+1,n):
        if (a[i] + a[j]) in a:
            print(a.index(a[i]+a[j])+1,i+1,j+1)
            exit(0)
print(-1)