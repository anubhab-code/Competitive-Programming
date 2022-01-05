for _ in range(int(input())):
    l = list(map(int,input().split()))
    l=sorted(l)
    if (l[0]==l[2] and l[1]%2==0) or (l[2]==l[1] and l[0]%2==0) or (l[0]==l[1] and l[2]%2==0):
        print("YES")
    elif (l[2] == l[0]+l[1]):
        print("YES")
    else:
        print("NO")
    