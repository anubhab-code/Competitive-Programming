s=input()
ans=1
c=1
for i in range(1,len(s)):
  if int(s[i])+int(s[i-1])==9:
      c+=1
  elif c%2==1:
      ans*=c//2+1;c=1
  else:
      c=1
if c%2==1:
    ans*=c//2+1
print(ans)