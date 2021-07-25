from typing import Counter
n=int(input())
l=list(map(int,input().split()))
ans=((n)*(n-1))//2
c=Counter(l)
for i in c.values():
  if i>=2:
    ans-=((i)*(i-1))//2
print(ans)