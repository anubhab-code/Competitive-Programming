for _ in range(int(input())):
    x,y=map(int,input().split())
    if x%2==0 and y%2==0:
        print(x//2,y//2)
    elif (y%2==1 and x%2==0) or (y%2==0 and x%2==1):
        print(-1,-1)
    else:
        if x<y:
            print(x,(y-x)//2)
        else:
            print((x-y)//2,y)