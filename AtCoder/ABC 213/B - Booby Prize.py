n=int(input())
l=list(map(int,input().split()))
temp=sorted(l)
print(l.index(temp[-2])+1)