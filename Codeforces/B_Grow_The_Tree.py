n = int(input())
l = sorted(list(map(int,input().split())))
a = sum(l[0:n//2])
b = sum(l[n//2:])
print(a**2+b**2)
