from itertools import accumulate
n=2*10**6
a,b,k=map(int,input().split())
prime=[1]*n
prime[1]=0
prime[0]=0
for i in range(2,n):
    if prime[i]==1:
        for j in range(i*i,n,i):
            prime[j]=0
prime=list(accumulate(prime))
l=1
r=b-a+1
ans=-1
while(l<=r):
    mid=(l+r)//2
    f=0
    for i in range(a,b-mid+2):
        x=i
        if prime[x+mid-1]-prime[x-1]<k:
            f=1
    if f==1:
        l=mid+1
    else:
        r=mid-1
        ans=mid
print(ans)