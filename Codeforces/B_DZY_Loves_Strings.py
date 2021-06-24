s=input()
k=int(input())
l=list(map(int,input().split()))
initial=0
c=1
for i in s:
    ind=ord(i)-97
    initial+=l[ind]*c
    c+=1
print(initial+(((k*c)+(k*(k-1))//2)*max(l)))