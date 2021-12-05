for _ in range(int(input())):
    a,b,n = map(int,input().split())
    if a<b:
        a,b=b,a
    flag = 1
    while b!=0:
        if n>a:
            print("NO")
            flag = 0
            break
        if ((n-(a%b))%b==0):
            print("YES")
            flag = 0
            break
        temp=a%b
        a=b
        b=temp
    if flag:
        print("NO")