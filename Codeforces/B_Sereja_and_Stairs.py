n=int(input())
l=list(map(int,input().split()))
ans=[]
b=[]
for i in range(len(l)):
    if l[i] not in ans:
        ans.append(l[i])
    elif l[i] not in b:
        b.append(l[i])
ans=sorted(ans)
b=sorted(b)
if len(b)>0:
    if ans[-1]==b[-1] :
        b.pop(-1)
print(len(ans)+len(b))
print(*(ans+b[::-1]))