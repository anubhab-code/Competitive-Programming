n=int(input())
l=[]
i=n 
while i:
    l.append(i)
    i-=1
ans=l[0]
for i in range(1,n):
    ans+=(l[i]-1)*(i+1)+1
print(ans)