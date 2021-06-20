s = input()
for x in s:
	if x == 'H' or x == 'Q' or x == '9':
		print("YES")
		break
else:
	print("NO")