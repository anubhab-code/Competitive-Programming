n=int(input())
a=list(map(int,input().split()))
temp=[(a[i],i+1) for i in range(n)]
temp=sorted(temp)
x=[]
y=[]
sx=0
sy=0
for i in range(n):
    if sx>sy:
        y.append(temp[i][1])
        sy+=temp[i][0]
    else:
        x.append(temp[i][1])
        sx+=temp[i][0]
print(len(x))
print(*x)
print(len(y))
print(*y)