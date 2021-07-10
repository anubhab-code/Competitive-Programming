n,k = map(int,input().split())
l = []
i = 1 
while i*i<=n:
  if n%i==0: 
    l.append(i)
    if i!=n//i :
      l.append(n//i)
  i += 1
l=sorted(l)
if k<=len(l):
  print(l[k-1])
else:
  print(-1)