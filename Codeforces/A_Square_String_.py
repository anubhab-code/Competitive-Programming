for _ in range(int(input())):
    a=input()
    n=len(a)
    if n%2==0 and a[0:n//2]==a[n//2:n]:
        print("YES")
    else:
        print("NO")
    