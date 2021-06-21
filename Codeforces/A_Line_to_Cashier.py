n=int(input())
arr=list(map(int,input().split()))
m=[]
for i in range(n):
    add=0
    l=list(map(int,input().split()))
    add=sum(l)*5 + len(l)*15
    m.append(add)
print(min(m))