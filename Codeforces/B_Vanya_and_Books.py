n=int(input())
ans=0
l=len(str(n))
if l>1:
    for i in range(l-1):
        ans+=9*(10**i)*(i+1)
    ans += (n-int("9"*(l-1)))*l
else:
    ans=n
print(ans)