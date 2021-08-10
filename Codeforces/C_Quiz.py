mod = 10**9+9
n,m,k = map(int,input().split())
x = max(0,m-(n-n%k)//k*(k-1)-n%k)
res = ((((pow(2,x+1,mod))-2)%mod)*k)%mod
z = (m-x*k)%mod
res = (res+z)%mod
print(res)