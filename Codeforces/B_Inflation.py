def check(tot, arr, k):
	for i in range(len(arr)):
		if i == 0:
			continue
		if arr[i]*100 > tot * k:
			return False;
		tot += arr[i]
	return True;

for _ in range(int(input())):
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))
	tot = int(0)
	for i in arr:
		tot += i
	lo , hi = int(0), int(10**11)
	while lo != hi:
		mid = lo + (hi - lo) // 2
		if check(mid+arr[0], arr, k) == True:
			hi = mid
		else :
			lo = mid + 1
	print(lo)