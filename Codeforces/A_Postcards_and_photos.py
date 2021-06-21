s=input()
c=0
t=0
old=""
for i in s:
	if i==old:
		c+=1
	if c>=5 or i!=old:
		t+=1
		c=0
	old=i
print(t)