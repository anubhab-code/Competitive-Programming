n = int(input())
temp = [0]*6
for i in range(6):
    temp[i] = n%2
    n//=2
temp=temp[::-1]
temp[1],temp[5]=temp[5],temp[1]
temp[2],temp[3]=temp[3],temp[2]
temp=temp[::-1]
ans = 0
for i in range(6):
    ans+=((2**i)*temp[i])
print(ans)