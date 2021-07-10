import math
n,m = map(int,input().split())
x = sorted(list(map(int,input().split())))
p = list(map(int,input().split()))
g = x[0]
diff = []
for i in range(len(x)-1):
    diff.append(abs(x[i]-x[i+1]))
diff = sorted(diff)
g = diff[0]
for i in range(1,len(diff)):
    g = math.gcd(diff[i],g)
for i in range(len(p)):
    if p[i]<=g and g%p[i]==0:
        print("YES")
        print(x[0],i+1)
        exit()
print("NO")