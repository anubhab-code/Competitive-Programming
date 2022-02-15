for _ in range(int(input())):
    n=int(input())
    x,y=input(),input()
    z1,z2=0,0
    o1,o2=0,0
    flag=1
    c=0
    if x==y:
        flag=1
    else:
        for i in range(n):
            if x[i]=="0":
                z1+=1
            else:
                o1+=1
            if y[i]=="0":
                z2+=1
            else:
                o2+=1
            if abs(z1-o1)!=abs(z2-o2):
                flag=0
    c1=z1-o1
    c2=z2-o2
    if flag==0 or c1!=c2:
        print("NO")
    else:
        print("YES")