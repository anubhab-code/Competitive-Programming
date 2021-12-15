for _ in range(int(input())):
    a,b,c=map(int,input().split())
    z = max(max(a,b),c)
    l = [a==z,b==z,c==z]
    if a>=z:
        a = 0
    else:
        a = z+1-a
    if b<z:
        b = z+1-b
    else:
        b = 0
    if c>=z:
        c = 0
    else:
        c = z+1-c
    if l.count(1)>1:
        if l[0]:
            a+=1
        if l[1]:
            b+=1
        if l[2]:
            c+=1
    print(a,b,c)
    
        
