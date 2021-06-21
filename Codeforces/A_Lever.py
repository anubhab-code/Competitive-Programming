l=input()
check=l.find("^")
lf=0
rf=0
for i in range(len(l)):
    if l[i]!='=' and l[i]!='^':
        m=int(l[i])
        d=abs(check-i)
        f=m*d
        if i < check:
            lf += f
        else:
            rf += f

if lf == rf:
    print("balance")
elif lf > rf:
    print("left")
else:
    print("right")