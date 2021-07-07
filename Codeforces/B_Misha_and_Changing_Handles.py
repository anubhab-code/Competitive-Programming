n=int(input())
d={}
s=set()
for _ in range(n):
    x,y=map(str,input().split())
    d[x]=y
    s.add(x)
ans=[]
for i in d:
    if i not in s:
        continue
    s.remove(i)
    y=d[i]
    while y in d and y in s:
        s.remove(y)
        y=d[y]
    ans.append([i,y])
print(len(ans))
for j in ans:
    print(*j)