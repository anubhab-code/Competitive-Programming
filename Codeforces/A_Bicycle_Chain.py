n= int(input())
a= list(map(int, input().split()))
m= int(input())
b= list(map(int, input().split()))
l=[]
for j in b:
    for i in a:
        if not j%i:
            l.append(j//i)
print(l.count(max(l)))