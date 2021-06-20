n=list(map(int,input().split()))[0]
ans=0
for i in range(n):
    if input()[1]=="+":
        ans+=1
    else:
        ans-=1
print(ans)