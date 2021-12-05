for _ in range(int(input())):
    n = int(input())
    check = str(n)
    if n%2==0:
        print(0)
    elif int(check[0])%2==0:
        print(1)
    else:
        flag = 1
        for i in check:
            if int(i)%2==0:
                flag = 0
                break
        if not flag:
            print(2)
        else:
            print(-1)