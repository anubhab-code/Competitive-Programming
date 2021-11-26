import math
n = int(input())
cur = 2
for k in range(1,n+1):
	goal = ((k+1)**2)*(k**2)
	print(int((goal-cur)/k))
	cur = int(math.sqrt(goal))