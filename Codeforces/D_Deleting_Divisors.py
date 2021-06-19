for _ in range(int(input())):
    n=int(input())
    if n%2==0:
        check=0
        while n%2==0:
            n=n//2
            check+=1
        if n<=1:
            if check%2:
                print("Bob")
            else:
                print("Alice")
        else:
            print("Alice")
    else:
        print("Bob")