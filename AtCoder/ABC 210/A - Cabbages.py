a,b,c,d=map(int,input().split())
if a-b<0:
	b=a
print((abs(b-a)*d)+b*c)