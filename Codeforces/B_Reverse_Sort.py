for _ in range(int(input())):
    n=int(input())
    s=input()
    l=list(s)
    l=sorted(l)
    a1,a2=[],[]
    for i in range(n):
        if s[i]!=l[i] and s[i]=="1":
            a1.append(i+2-1)
    for i in range(n-1,-1,-1):
        if s[i]!=l[i] and l[i]=="1":
            a2 = [i+1]+a2
    if not (a1!=[] or a2!=[]):
        print(0)
    else:
        print(1)
        print(len(a1+a2),*a1,*a2)