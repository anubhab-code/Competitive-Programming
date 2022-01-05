for _ in range(int(input())):
  n=int(input())
  a=list(map(int,input().split()))
  tp=0
  for i in range(n):
    while a[i]%2==0:
      a[i]=a[i]//2
      tp=tp+1
  ans=sum(a)-max(a)+max(a)*(2**tp)
  print(ans)