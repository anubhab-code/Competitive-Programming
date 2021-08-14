for _ in range(int(input())):
    c,m,x= map(int,input().split())
    print(min(min(c,m),(c+m+x)//3))