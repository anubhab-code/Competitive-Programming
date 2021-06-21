home=[]
guest=[]
count=0
for i in range(int(input())):
    a,b=map(int,input().split())
    home.append(a)
    guest.append(b)
for j in range(len(home)):
    for k in range(len(home)):
        if home[j]==guest[k]:
            count+=1
print(count)