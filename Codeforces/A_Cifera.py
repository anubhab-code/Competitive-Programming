k=int(input())
l=int(input())
x,i=0,1
while x<l:
    x=k**i
    i+=1
if x==l:
    print("YES")
    print(i-2)
else:
    print("NO")