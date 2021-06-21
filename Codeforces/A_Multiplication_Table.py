n,x = map(int,input().split())
cnt = 0
for i in range(1,n+1):
    if(x%i == 0):
        check = x/i
        if(check<=n):
            cnt+=1
print(cnt)