n=int(input())
l=list(map(int,input().split()))
fives=0
zeros=0
for i in l:
    if i==5:
        fives+=1
    else:
        zeros+=1
if zeros==0:
    print(-1)
elif fives<9:
    print(0)
else:
    fives=fives-(fives%9)
    for i in range(fives):
        print(5,sep='',end='')
    for i in range(zeros):
        print(0,sep='',end='')