a,b = map(int,input().split())
a2,b2 = map(int,input().split())
a3,b3 = map(int,input().split())
check = 0
if a>=a2 and b>=b2:
    h1 = a-a2
    h2 = b-b2
    if (h2>=b3 and a>=a3) or (h2>=a3 and a>=b3) or (h1>=a3 and b>=b3) or (h1>=b3 and b>=a3):
        check = 1
if a>=b2 and b>=a2:
    h1 = a-b2
    h2 = b-a2
    if (h2>=b3 and a>=a3) or (h2>=a3 and a>=b3) or (h1>=a3 and b>=b3) or (h1>=b3 and b>=a3):
        check = 1
if check==1:
    print('YES')
else:
    print('NO')