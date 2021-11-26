n = int(input())
vis = [0]*1000001
ans,occ = 0,0
for i in range(n):
    a,b = map(str,input().split())
    b=int(b)
    if a=="+":
        vis[b]=1
        if ans==occ:
            ans+=1
            occ+=1
        else:
            occ+=1
    else:
        if vis[b]==0:
            ans+=1
        else:
            occ-=1
print(ans)