for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l=sorted(l)
    for j in range(n):
        print(l[j], l[(2*n)-(j+1)], end=" ")
    print()