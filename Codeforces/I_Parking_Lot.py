n=int(input())
ans=24*(4**(n-3))
if n>3:
    ans+=(n-3)*36*4**(n-4)
print(ans)