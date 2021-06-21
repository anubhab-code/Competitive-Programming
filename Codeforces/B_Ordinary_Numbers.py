for i in range(int(input())):
    n=int(input())
    converted=str(n)
    c=0
    for j in converted:
        c+=1
    f=n//(10**(c-1))
    if n>9:
        if int(str(f)*c)>n:
            print((c-1)*9 +f-1)
        else:
            print((c-1)*9 +f)
    else:
        print(n)