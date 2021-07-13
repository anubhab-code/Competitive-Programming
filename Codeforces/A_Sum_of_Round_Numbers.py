for _ in range(int(input())):
    x=int(input())
    n=x
    c=1
    d=[]
    while n:
        if n%10:
            a=(n%10)*c
            d.append(str(a))
            n=n//10
            c*=10
        elif n%10==0:
            c*=10
            n//=10
    print(len(d))
    print(" ".join(d))