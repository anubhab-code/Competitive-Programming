s = input()
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
c=0
for i in d:
    if d[i]%2!=0:
        c+=1
        
if c==0 or c==1:
    print('First')
else:
    if c%2==0:
        print('Second')
    else:
        print('First')