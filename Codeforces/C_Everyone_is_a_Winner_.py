for _ in range(int(input())):
	n=int(input())
	s=set([0])
	for i in range(1,int(n**0.5)+1):
		s.add(i)
		s.add(n//i)
	s=list(s)
	s.sort()	
	print(len(s))
	print(*s)