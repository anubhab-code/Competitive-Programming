import math
for _ in range(int(input())):
  n = int(input())
  ans = math.floor(math.sqrt(2*n-1))
  print((ans-1)//2)