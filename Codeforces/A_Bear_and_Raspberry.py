n,c=map(int,input().split())
profit=[0]
a=[int(x) for x in input().split()]
for i in range(len(a)-1):
    if a[i]-a[i+1]-c>0:
        profit.append(a[i]-a[i+1]-c)
print(max(profit))