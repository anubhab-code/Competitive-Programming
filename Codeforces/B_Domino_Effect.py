n=int(input())
s=input()
c=0
m,l,r=0,-1,-1
for i in range(n):
    if c==0:
        if s[i]=='R':
            m+=i
            c=1
            r=i
        elif s[i]=='L':
            c=1
            l=i
    elif r>-1 and s[i]=='L':
        if (i-r)%2==0:
            m+=1
        r=-1
        l=i
    elif l>-1 and s[i]=='R':
        m+=i-l-1
        l=-1
        r=i
if l>-1 :
    m+=len(s)-l-1
if s.count(".")==n:
    print(n)
else: 
    print(m)