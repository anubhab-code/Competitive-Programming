import math 
for _ in range(int(input())):
	n=int(input())
	fact=[]
	even=0
	if n==1:
		print('FastestFinger')
		continue
	elif n%2!=0 or n==2:
		print('Ashishgup')
		continue
	while n>1:
		for i in range(2,int(math.sqrt(n))+2):
			if n%i==0:
				if i%2!=0:
					fact.append(i)
				else:
					even+=1
				n=n//i
				break
		else:
			fact.append(n)
			break
	if len(fact)>=1 and even>1:
		print('Ashishgup')
	elif len(fact)>1 and even==1:
		print('Ashishgup')
	else:
		print('FastestFinger')