n=int(input())
l=list(map(int,input().split()))
l.sort()
c=1
for i in range(n):
  c*=l[i]-i
  c = (c+1000000007)%1000000007
print(c)