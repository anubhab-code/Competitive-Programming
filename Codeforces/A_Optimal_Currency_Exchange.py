n = int(input())
d = int(input())
e = int(input())
e*=5
ans = min(n%d,n%e)
rem = n%d
while rem<=n:
    if (rem//e)%5==0:
        ans = min(ans,rem%e)
    rem+=d
rem = n%e
while rem<=n:
    ans = min(ans,rem%d)
    rem+=e
print(ans)