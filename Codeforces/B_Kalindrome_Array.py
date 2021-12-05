for _ in range(int(input())):
    n=int(input())
    l = list(map(int,input().split()))
    flag=1
    i,j,k=0,n-1,0
    while i<j:
        if l[i]==l[j]:
            pass
        else:
            if k == 0:
                k = l[j]
                j-=1
                continue
            elif k == l[j]:
                j-=1
                continue
            elif k == l[i]:
                i+=1
                continue
            else:
                flag = 0
                break
        i+=1
        j-=1
    f2 = 1
    i,j,k=0,n-1,0
    while i<j:
        if l[i]==l[j]:
            pass
        else:
            if k == 0:
                k = l[i]
                i+=1
                continue
            elif k == l[i]:
                i+=1
                continue
            elif k == l[j]:
                j-=1
                continue
            else:
                f2 = 0
                break
        i+=1
        j-=1
    if not (flag or f2):
        print("NO")
    else:
        print("YES")
