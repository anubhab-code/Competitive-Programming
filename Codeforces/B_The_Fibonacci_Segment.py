n=int(input())
l=list(map(int,input().split()))
ans=2
c=2
if n==1:
    ans=1
else:
    for i in range(2,n):
        if l[i]== l[i-1]+l[i-2]:
            c+=1
        else:
            c=2
        ans=max(ans,c)
print(ans)