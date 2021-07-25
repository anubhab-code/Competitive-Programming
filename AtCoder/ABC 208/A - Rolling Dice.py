a,b = list(map(int,input().split()))
if b <= 6 * a and b >= a:
    print("Yes")
else:
    print("No")