for _ in range(int(input())):
    a,b = map(int,input().split())
    if a//2 + a%2 >=b:
        l = [["." for i in range(a)] for j in range(a)]
        k = 0
        for i in range(0,a,2):
            if k<b:
                l[i][i] = "R"
                k += 1
            else:
                break
        for i in l:
            print("".join(i))
    else:
        print(-1)