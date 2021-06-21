a,b=map(int,input().split())
counta=0
countb=0
countc=0
for i in range(1,7):
    if abs(a-i)<abs(b-i):
        counta+=1
    elif abs(a-i)>abs(b-i):
        countb+=1
    else:
        countc+=1
print(counta,countc,countb)