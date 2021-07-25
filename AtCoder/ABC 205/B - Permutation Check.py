n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
a=[]
for i in range(1,n+1):
  a.append(i)
if a==l:
  print("Yes")
else:
  print("No")
  