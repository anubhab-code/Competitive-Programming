import sys
sys.stdin = open('input.txt', 'r') 
sys.stdout = open('output.txt', 'w')
for i in range(int(input())):
	n = int(input())
	if n%2 == 0:
		print(1)
	else:
		print(0)