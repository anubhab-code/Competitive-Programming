for _ in range(int(input())):
    n,k1,k2=map(int,input().split())
    w,b=map(int,input().split())
    check=2*n-(k1+k2)
    if (k1+k2)//2>=w and check//2>=b:
        print("YES")
    else:
        print("NO")