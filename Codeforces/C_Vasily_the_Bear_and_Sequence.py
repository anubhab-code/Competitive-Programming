x=int(input())
s=list(map(int,input().split()))
ans=[]
for u in range(0,30):
    cur=(1<<(u))
    v=(1<<(u+1))-1
    tem=[]
    for n in s:
        if n&(cur):
            tem.append(n)
    for n in tem:
        v&=n
    if v%(1<<(u))==0:
        ans=tem
print(len(ans))
print(*ans)
