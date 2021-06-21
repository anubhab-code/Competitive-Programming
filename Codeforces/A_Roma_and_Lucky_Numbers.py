n,k=input().split()
l=input().split()
c=0
for i in l:
	if i.count("4")+i.count("7")>int(k):
		c+=1
print(len(l)-c)