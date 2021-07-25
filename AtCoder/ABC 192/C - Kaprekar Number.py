n,k=map(int,input().split())
temp=n
def rr(a):
  des=int("".join(sorted(str(a), reverse=True)))
  asc=int("".join(sorted(str(a))))
  f=des-asc
  return f
for i in range(k):
  temp=rr(n)
  n=rr(n)
print(temp)