s=list(input())
t=list(input())
count=1
for i in t:
	if i==s[0]:
		count+=1
		s.pop(0)
print(count)