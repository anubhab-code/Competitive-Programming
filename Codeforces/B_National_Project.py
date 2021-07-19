import math
for _ in range(int(input())):
	n,g,b = list(map(int,input().split()))
	h = math.ceil(n/2)
	gd = math.ceil(h/g)
	wd = b*(gd-1)
	good = g*gd
	eg = good-h
	ans = good+wd-eg
	if ans>n:
		print(ans)
	else:
		print(n)