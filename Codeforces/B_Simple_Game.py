n,m=map(int,input().split())
mid=n//2
if n==1 and m==1:
    print("1")
elif mid<m:
    print(m-1)
else:
    print(m+1)