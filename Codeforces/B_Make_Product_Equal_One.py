n=int(input())
l=list(map(int,input().split()))
ans=0
neg,z=0,0
for i in l:
    if i==0:
        z+=1
    elif i<0:
        neg+=1
    ans+=abs(abs(i)-1)
if neg%2==1 and z==0:
    ans+=2
print(ans)