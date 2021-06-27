def fun(n):
    s = str(n)
    ans = 0
    for i in s:
        ans += int(i)
    return ans
    
n = int(input())
flag = 0
x = int(n**0.5)
for i in range(x-90,x+1):
    for j in range(x,x+90):
        if i*j==n and j-i==fun(i):
            flag = 1
            break
    if flag==1:
        break
if flag==1:
    print(i)
else:
    print(-1)


# from math import *
# n=int(input())
# nr=int(sqrt(n))
# l=len(str(nr))
# p=True
# for i in range (1,9*l +1 ):
#     zz=i**2 + 4*n
#     zzz=int(zz**0.5)
#     if zz==(zzz**2):
#         a=(-i+zzz)/2
#         aa=int(a)
#         st=str(aa)
#         l=list(map(int,st))
#         if a==aa and i==sum(l):
#             print(aa)
#             p=False
#             break
# if p:
#     print(-1)