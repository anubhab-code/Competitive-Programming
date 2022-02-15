from math import ceil
for _ in range(int(input())):
    n = int(input())
    print(2)
    ans = n
    for i in range(n-1,0,-1):
        print(ans,end=" ")
        print(i)
        ans = int(ceil((ans+i)/2))