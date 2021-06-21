l = []
for _ in range(5):
	blah = list(map(int,input().split()))
	l.append(blah)
x=0
y=0
for i in range(5):
	for j in range(5):
		if l[i][j] == 1:
			x = i
			y = j
			break
print(abs(x-2)+abs(y-2))