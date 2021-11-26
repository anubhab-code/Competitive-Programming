n = int(input())
l = list(map(int,input().split()))
if n%2==0 or l[0]%2==0 or l[-1]%2==0:
    print("NO")
else:
    print("YES")