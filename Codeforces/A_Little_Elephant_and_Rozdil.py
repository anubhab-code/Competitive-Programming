n=int(input())
z=list(map(int,input().split()))
k=min(z)
if z.count(k)>=2:
	print("Still Rozdil")
else:
    print(z.index(k)+1)