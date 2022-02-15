a,b = map(int,input().split())
for i in range(1,10000):
    a*=3
    b*=2
    if a>b:
        print(i)
        break