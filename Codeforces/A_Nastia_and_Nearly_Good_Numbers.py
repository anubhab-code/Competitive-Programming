for i in range(int(input())):
    a,b=map(int,input().split())
    if b<=1:
        print("NO")
        continue
    print("YES")
    print(a , b*a , a*(b+1))