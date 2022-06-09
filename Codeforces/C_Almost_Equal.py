n=int(input())
if n%2==1:
    print("YES")
    ans=[]
    for i in range(n):
        ans.append(2*(i+1)-1)
    for i in range(n):
        ans.append(2*(i+1))
    for i in range(1,n,2):
        ans[i],ans[n+i]=ans[n+i],ans[i]
    print(*ans)
else:
    print("NO")