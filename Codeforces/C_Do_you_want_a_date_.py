MOD = 1000000007
n = int(input())
l = list(map(int,input().split()))
l=sorted(l)
mi = 0
ma = 0
for i in range(n): 
    ma = (l[n-i-1]+2*ma)%MOD
    # print(ma)
    mi = (l[i]+2*mi)%MOD
    # print(mi)
print((ma-mi)%MOD)