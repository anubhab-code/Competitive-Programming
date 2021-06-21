a=input()
b=input()
c=int(a)+int(b)
a1=a.replace('0','')
b1=b.replace('0','')
c1=str(c).replace('0','')
if int(a1)+int(b1)==int(c1):
    print("YES")
else:
    print("NO")