s1=input()
s2=input()
a=len(s1)
b=len(s2)
if a!=b:
    print("NO")
else:
    c=0
    for i in range(a):
        if s1[i]!=s2[i]:
            if c==0:
                x1,x2=s1[i],s2[i]
            elif c==1:
                y1,y2=s1[i],s2[i]

            c=c+1
    if c==2:
        if x1==y2 and x2==y1:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")