x = abs(int(input()))
ans,curr = 0,0
while curr<x or (x-curr)%2!=0:
    ans+=1
    curr+=ans
print(ans)