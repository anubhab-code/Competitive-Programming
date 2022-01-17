s = input()
x,y = 1,1
for i in s:
    if i=='1':
        print(4,y)
        y+=2
        if y==5:
            y=1
    else:
        print(1,x)
        x+=1
        if x==5:
            x=1 