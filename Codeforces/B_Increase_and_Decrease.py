n=int(input())
a=sum(map(int,input().split()))
if a%n!=0:
  print(n-1)
else:
  print(n)