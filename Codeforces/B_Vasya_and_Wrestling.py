a=[]
b=[]
last=0
one=0
two=0
for _ in range(int(input())):
    n=int(input())
    if n>0:
        one+=n
        a.append(n)
        last=1
    else:
        two+=-n
        b.append(-n)
        last=2
if one>two:
    print('first')
elif one==two:
    if a!=b:
        for j in range(min(len(a),len(b))):
            if a[j]>b[j]:
                print('first')
                break
            elif b[j]>a[j]:
                print('second')
                break
    else:
        if last==1:
            print('first')
        else:
            print('second')
else:
    print('second')