n=int(input())
n=n+1
l1=list(map(int,input().split()))
count=sum(l1)
c=0
for i in range(1,6):
  total=i+count
  if total%n!=1:
    c=c+1
print(c)