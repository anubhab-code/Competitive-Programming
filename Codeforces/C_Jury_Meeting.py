mod=998244353

def power(x,y,p):
    res=1
    x=x%p
    while y>0:
        if y&1:
            res = (res * x) % p
        y=y>>1
        x=(x*x)%p
    return res

def modinv(n,p):
    return power(n,p-2,p)

def ncr(n,r,p):
    if n<r:
        return 0
    if r==0:
        return 1
    return (fac[n]*modinv(fac[r],p)%p*modinv(fac[n-r],p)%p)%p

def fun():
    n=int(input())
    a=list(map(int,input().split()))
    a=sorted(a)
    if a[n-1]-a[n-2]>1:
        print(0)
        return
    if n==1:
        print(1)
    elif a[n-1]==a[n-2]:
        print(fac[n])
    else:
        nu=0
        for i in range(n):
            if a[i]<a[n-2]:
                nu+=1
        ans=fac[n]
        to=0
        for i in range(nu+1):
            xo= (fac[n-i-1]*ncr(nu,i,mod))%mod
            xo= (xo*fac[i])%mod
            to= (to + xo)%mod
        print((ans-to+mod)%mod)

fac=[0]*200007
fac[0]=1
for i in range(1,200007):
    fac[i]=(fac[i-1]*i)%mod
for _ in range(int(input())):
    fun()
    
