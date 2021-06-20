import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")
n=input()
for _ in range(3):
	a,b=input().split()
	if a==n:n=b
	elif b==n:n=a
print(n)