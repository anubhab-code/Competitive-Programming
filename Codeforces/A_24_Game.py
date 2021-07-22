n=int(input())
if n>=4:
    print("YES")
    if n==4:
        print("4 * 3 = 12")
        print("12 * 2 = 24")
        print("24 * 1 = 24")
    elif n==5:
        print("5 * 4 = 20")
        print("20 + 3 = 23")
        print("23 + 2 = 25")
        print("25 - 1 = 24")
    else:
        print("4 * 3 = 12")
        print("12 * 2 = 24")
        print(str(n)+" - "+str(n-1)+" = 1")
        print("1 - 1 = 0")
        for i in range(5,n-1):
            print(str(i)+" * 0 = 0")
        print("24 + 0 = 24")
else:
    print("NO")