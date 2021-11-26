l=[]
for i in range(2):
    a,b=input(),input()
    # print(a,b)
    temp=list(b[0]+a+b[1])
    # print(temp)
    temp.remove("X")
    # print(temp)
    while temp[0]!="A":
        temp[0],temp[1],temp[2]=temp[2],temp[0],temp[1]
    l.append("".join(temp))
if l[0]==l[1]:
    print("YES")
else:
    print("NO")
