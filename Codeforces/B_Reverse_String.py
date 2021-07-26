for _ in range(int(input())):
	s1 = input()
	s2 = input()
	flag = 0
	for i in range(len(s1)):
		for j in range(len(s1)-i):
			check = len(s2)-1-j
			if i+j < check:
				continue                                 
			a = i
			b = i+j-check
			c = i+j
			if s1[a:c+1] + s1[b:c][::-1] == s2:
				flag = 1	
	if flag==1:
	    print("YES")
	else:
	    print("NO")