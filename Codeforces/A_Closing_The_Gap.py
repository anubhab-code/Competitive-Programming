for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    if sum(l)%n==0:
        print(0)
    else:
        print(1)