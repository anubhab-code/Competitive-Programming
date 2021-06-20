n=int(input())
num=input()
a=sorted(num[:n])
b=sorted(num[n:])
d=zip(a,b)
s1,s2=0,0
for i,j in d:
    if i<j:
        s1+=1
    elif i>j:
        s2+=1
if s1==n or s2==n:
    print('YES')
else:
    print('NO')
