n = int(input())
s = input()
if n%2==1:
    print("No")
else:
    t,check=0,0
    for i in range(len(s)):
        if s[i]=="(":
            t+=1
        if s[i]==")":
            t-=1
        if t<-1:
            check+=1
            break
    if t>0:
        check+=1
    if check!=0:
        print("No")
    else:
        print("Yes")