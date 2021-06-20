n=int(input())
lis=[]
for i in range(n):
    st=""
    st+="  "*(n-i)
    for j in range(0,i+1):
        st+=str(j)
        st+=" "
    for j in range(i-1,-1,-1):
        st+=str(j) 
        st+=" "
    st=st[:len(st)-1]
    lis.append(st)
for i in lis:
    print(i)
mid_str=""
for i in range(0,n+1):
    mid_str+=str(i)+" "
for i in range(n-1,-1,-1):
    mid_str+=str(i)+" "
mid_str=mid_str[:len(mid_str)-1]
print(mid_str)
lis.reverse()
for i in lis:
    print(i)