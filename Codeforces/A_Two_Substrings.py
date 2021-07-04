l=input()
n=len(l)
f=0
prev=0
found=0
for i in range(n-1):
    if l[i:i+2]=='AB':
        if f==0:
            prev=i+1
            f=1
        else:
            continue
    elif l[i:i+2]=='BA':
        if f==1:
            if i!=prev:
                found=1
            else:
                continue

prev=0
f=0
for i in range(n-1):
    if l[i:i+2]=='BA':
        if f==0:
            prev=i+1
            f=1
        else:
            continue
    elif l[i:i+2]=='AB':
        if f==1:
            if i!=prev:
                found=1
            else:
                continue

if found:
    print('YES')
else:
    print('NO')