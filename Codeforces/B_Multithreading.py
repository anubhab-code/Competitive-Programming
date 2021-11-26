n = int(input())
l = list(map(int,input().split()))
ans = n-1
while ans>0 and l[ans-1]<l[ans]:
	ans-=1
print(ans)
