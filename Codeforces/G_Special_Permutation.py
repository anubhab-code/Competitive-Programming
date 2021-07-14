for _ in range(int(input())):
  n=int(input())
  ans=[]
  if n<4:
    print(-1)
  else:
    if n&1:
      for i in range(n,0,-2):
        ans.append(i)
      ans.append(4)
      ans.append(2)
      for i in range(6,n,2):
        ans.append(i)
    else:
      for i in range(n-1,0,-2):
        ans.append(i)
      ans.append(4)
      ans.append(2)
      for i in range(6,n+1,2):
        ans.append(i)
    print(*ans)