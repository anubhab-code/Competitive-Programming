a,b=map(int,input().split(" "))
done={a}
c=0
while a!=0:
    c+=1
    if c>2*b:
        break
    a+=a%b
    if a in done:
        print("Yes")
        exit()
    done.add(a)
print("No")