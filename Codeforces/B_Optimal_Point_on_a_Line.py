n=int(input())
l=list(map(int,input().split()))
print(sorted(l)[(n-1)//2])