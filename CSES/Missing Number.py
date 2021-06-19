n=int(input())
l=list(map(int,input().split()))
print(int((n*(n+1))/2)-sum(l))