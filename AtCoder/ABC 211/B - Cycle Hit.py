s1=input()
s2=input()
s3=input()
s4=input()
l=[]
l.append(s1)
l.append(s2)
l.append(s3)
l.append(s4)
if l.count('H')==1 and l.count('2B')==1 and l.count('3B')==1 and l.count('HR')==1:
  print("Yes")
else:
  print("No")
