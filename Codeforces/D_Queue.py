t=int(input())
l=list(map(int,input().split()))
l=sorted(l)
ans=0
c=0
for i in l:
   if i>=c:
       ans+=1
       c+=i
print(ans)