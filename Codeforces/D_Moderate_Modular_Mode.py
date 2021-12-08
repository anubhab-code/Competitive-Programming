for _ in range(int(input())):
    a,b=map(int,input().split())
    if a<=b:
        b-=(((a+b)//2)%a)+1
        b+=1
        print(b)
    else:
        print(a+b)