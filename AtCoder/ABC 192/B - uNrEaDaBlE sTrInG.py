s=input()
def check(string):
  for i in range(0,len(string)):
    if (i%2==0) and string[i].isupper():
      return False
    elif (i%2==1) and string[i].islower():
      return False
  return True
if(check(s)):
  print('Yes')
else:
  print('No')