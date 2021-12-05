for _ in range(int(input())):
    x,y=map(int,input().split())
    print(min(min(x,y),(x+y)//4))