for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    new=a[0]
    print(0,end=" ")
    for j in range(1,n):
        f=new & a[j]
        f=f^new
        print(f,end=' ')
        new=f^a[j]
    print()