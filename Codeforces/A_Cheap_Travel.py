import math
n,m,a,b = map(int,input().split())
cost1 = (n//m)*b + (n%m)*a
cost2 = a*n
cost3 = int((math.ceil(float(n)/m))*b)	
print(int(min(cost1,cost2,cost3)))