n,v=map(int,input().split())
l=[]
count=0
for i in range(n):
    m=min(list(map(int,input().split()))[1:])
    count+=1
    if v>m:
        l.append(count)
print(len(l))
print(*l)