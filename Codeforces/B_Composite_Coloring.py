primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
for _ in range(int(input())):
	n = int(input())
	l = list(map(int,input().split()))
	ind = [0]*11
	done = 0
	ans = []
	for i in range(n):
		for k in range(11):
			if l[i]%primes[k]==0:
				if ind[k]==0:
					done+=1
					ind[k]=done
					ans.append(ind[k])
				else:
					ans.append(ind[k])
				break
	print(len(set(ans)))
	print(*ans)