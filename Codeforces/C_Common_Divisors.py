import math
n=int(input())
a=list(map(int,input().split()))
g=0
for i in a:
  g=math.gcd(i,g)
ans=set()
for i in range(1,int(g**0.5)+1):
  if g%i==0:
    ans.add(i)
    ans.add(g//i)
print(len(ans))