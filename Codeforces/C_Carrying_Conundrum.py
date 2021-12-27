for _ in range(int(input())):
    n=input()
    n1=''
    n2=''
    l=len(n)
    for i in range(l):
        if i%2==0:
            n1+=n[i]
        else:
            n2+=n[i]
    if len(n2)==0:
        print(int(n1)-1)
    else:
        n1=int(n1)
        n2=int(n2)
        print((n1+1)*(n2+1)-2)