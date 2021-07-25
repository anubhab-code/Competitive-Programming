n,x = list(map(int,input().split()))
data = list(map(int,input().split()))
if sum(data) - (n//2) <= x:
    print("Yes")
else:
    print("No")