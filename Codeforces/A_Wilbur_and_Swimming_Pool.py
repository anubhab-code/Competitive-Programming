n=int(input())
a,b=[],[]
for i in range(n):
    x,y=map(int,input().split())
    a.append(x)
    b.append(y)
check=(max(a)-min(a))*(max(b)-min(b))
if check==0:
    print(-1)
else:
    print(check)