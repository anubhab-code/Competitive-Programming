n=int(input())
l=list(map(int,input().split()))
s=[]
ans=1
for i in range(n):
    if l[i]==1:
        if s!=[]:
            temp=i-s[-1]
            ans=ans*temp
        s.append(i)
if s==[]:
    print(0)
else:
    print(ans)
    