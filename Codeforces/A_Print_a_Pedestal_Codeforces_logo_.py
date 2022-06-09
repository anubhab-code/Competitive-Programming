for _ in range(int(input())):
    n = int(input())
    n -= 3
    t1,t2,t3 = n//3+1,n//3+2,n//3
    if n%3==2:
        print(t1+1,t2+1,t3)
    elif n%3==1:
        print(t1,t2+1,t3)
    else:
        print(t1,t2,t3)