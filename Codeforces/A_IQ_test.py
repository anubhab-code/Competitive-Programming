n=int(input())
num=list(map(int,input().split()))
blank=[]
for i in num:
    if i%2==0:
        blank.append(0)
    else:
        blank.append(1)
if blank.count(0)>blank.count(1):
    print(blank.index(1)+1)
else:
    print(blank.index(0)+1)