n = int(input())
l = list(map(int, input().split()))
flag = 0
for i in range(1,max(l)+1):
    for j in range(n):
        if i>l[j]:
            l[j] = 0
    for j in range(n-1):
        if l[j] == l[j+1]==0 or l[n-1]==0 or l[0] == 0:
            flag = 1
            break
    if flag == 1:
        break
if n==1:
    print(l[0])
else:
    print(i-1)


# n=int(input())
# l=list(map(int,input().split()))
# i=1
# ll=l[0]
# while(i<n-1):
#     if (l[i]>l[i+1]):
#         if l[i]<ll:
#             ll=l[i]
#         i+=1
#     else:
#         if l[i+1]<ll:
#             ll=l[i+1]
#         i+=2
# if l[n-1]<ll:
#     ll=l[n-1]
# print(ll)