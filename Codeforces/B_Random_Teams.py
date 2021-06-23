n, m = map(int, input().split())
maxi = n - m + 1
maxi = maxi*(maxi-1)//2
mini = n//m
rem = n%m
mini = (m-rem)*(mini*(mini-1)//2) + rem*(mini*(mini+1)//2)
print(mini, maxi)