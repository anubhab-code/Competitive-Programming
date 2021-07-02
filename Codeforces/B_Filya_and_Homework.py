n=int(input())
l=list(map(int,input().split()))
a=(max(l)+min(l))/2
ans=[]
for i in l:
    ans.append(abs(a-i))
new=list(set(ans))
if new.count(0)==1:
    new.remove(0)
if len(new)>1:
    print("NO")
else:
    print("YES")