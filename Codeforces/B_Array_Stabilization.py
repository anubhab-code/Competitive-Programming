n = int(input())
l = list(map(int,input().split()))
l = sorted(l)
a = l[n-2]-l[0]
b = l[n-1]-l[1]
print(min(a,b))