m = 1000000007
def hehe(a,b):
    a%=m
    res=1
    while b>0:
        if b&1:
            res=(res*a)%m
        a= (a*a)%m
        b>>=1
    return res
 
n = int(input())
ans= hehe(2,n)%m
print(int((ans*(ans+1)//2)%m))