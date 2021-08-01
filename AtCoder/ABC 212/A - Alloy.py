a,b=map(int,input().split())
if b==0 and a>0:
  print("Gold")
elif a==0 and b>0:
  print("Silver")
elif a>0 and b>0:
  print("Alloy")
  