for _ in range(int(input())):
    n=int(input())
    a=list(input())
    b=list(input())
    flag1=1
    steps=[]
    for i in range(n):
        flag=0
        if a[i]==b[i]:
            continue
        for j in range(i+1,n):
            if a[j]!=b[j] and a[j]==a[i]:
                steps.append((j+1,i+1))
                a[j],b[i]=b[i],a[j]
                flag=1
                break
        if flag==0:
            for j in range(i + 1, n):
                if b[j] != a[j] and b[j] == a[i]:
                    steps.append((j + 1, j + 1))
                    a[j], b[j] = b[j], a[j]
                    steps.append((j + 1, i+ 1))
                    a[j], b[i] = b[i], a[j]
                    flag = 1
                    break
        if flag==0:
            flag1=0
            break
    if flag1==0:
        print("No")
    else:

        print("yes")
        print(len(steps))
        for i in steps:
            print(*i)