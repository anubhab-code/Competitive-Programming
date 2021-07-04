r,g,b = map(int,input().split())
l=[]
for i in range(min(r+1,g+1,b+1,3)):
    l.append(i+(r-i)//3+(g-i)//3+(b-i)//3)
print(max(l))