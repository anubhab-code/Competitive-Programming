n = int(input())
ans,x,y = 0,0,0
for i in range(n):
    if i==0:
        x,y = map(int,input().split())
        ans += min(x,y)+1
    else:
        a,b = map(int,input().split())
        if a==x and b==y:
            continue
        da = a-x
        db = b-y
        if x<y:
            diff = abs(x-y)
            if diff<=da:
                ans+=1
                da-=diff
            else:
                da = 0
        elif x>y:
            diff = abs(x-y)
            if diff<=db:
                ans+=1
                db-=diff
            else:
                db = 0
        ans+=min(da,db)
        x,y=a,b
print(ans)