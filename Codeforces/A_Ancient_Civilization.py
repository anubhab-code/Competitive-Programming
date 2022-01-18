for _ in range(int(input())):
    n,k = map(int,input().split())
    a1 = list(map(int,input().split()))
    a2 = [0]*k
    for i in range(n):
        temp = 0
        while a1[i]!=0:
            if not a1[i]%2==1:
                pass
            else:
                a2[temp]+=1
            a1[i]//=2
            temp+=1
    res = ""
    for i in a2:
        if not i>n//2:
            res = "0"+res
        else:
            res = "1"+res
    ans=int(res,2)
    print(ans)