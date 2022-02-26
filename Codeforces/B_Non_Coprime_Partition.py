n = int(input())
if n == 1 or n == 2:
    print("No")
else:
    even,odd = [],[]
    ec,oc = 0,0
    for i in range(1,n+1):
        if i%2==1:
            odd.append(i)
            oc += 1
        else:
            even.append(i)
            ec += 1
    print("Yes")
    print(oc, *odd)
    print(ec, *even)