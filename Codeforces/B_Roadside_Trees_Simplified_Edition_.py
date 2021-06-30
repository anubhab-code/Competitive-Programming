pre,ans=0,-1
for i in range(int(input())):
    n=int(input())
    ans+=abs(n-pre)
    ans+=2
    pre=n
print(ans)