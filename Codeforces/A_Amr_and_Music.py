a,b=map(int,input().split())
l=list(map(int,input().split()))
k,s=[],0
for i in range(len(l)):
    k.append([l[i],i+1])
g=sorted(k,key=lambda i:i[0])
ans=[]
c=0
for i in g:
    s+=i[0]    
    if s>b:
        break
    ans.append(i[1])
    c+=1
print(c)
if len(ans)>0:
    ans=sorted(ans)
    print(*ans)