a,b = input().split('e')
a1,a2 = a.split('.')
if b=='0':
    if a2=='0':
        print(a1)
    else:
        print(a)
else:
    if len(a2)<= int(b):
        s = int(b)-len(a2)
        print(int(a1+a2+'0'*s))
    else:
        s = int(b)
        print(a1+a2[:s]+'.'+a2[s:])