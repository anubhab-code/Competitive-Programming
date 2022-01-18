for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if 2*b<a+c:
        if (a+c)%(2*b) != 0:
            print("NO")
        else:
            print("YES")
    elif 2*b==a+c:
        print("YES")
    else:
        b = 2*b
        if (b-c)%a==0:
            print("YES")
        elif (b-a)%c==0:
            print("YES")
        else:
            print("NO")