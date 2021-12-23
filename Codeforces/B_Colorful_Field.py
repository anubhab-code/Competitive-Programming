n,m,k,t=map(int,input().split())
w=[]
for _ in range(k):
    a,b=map(int,input().split())
    w.append([a,b])
for _ in range(t):
    flag=1
    x,y=map(int,input().split())
    t=[x,y]
    for i in range(k):
        if t==w[i]:
            flag=0
            break
    if flag==0:
        print("Waste")
    else:
        c=(x-1)*m+(y-1)
        wc=0
        for i in range(k):
            if w[i][0]<x:
                wc+=1
            elif w[i][0]==x:
                if w[i][1]<=y:
                    wc+=1
            else:
                continue
        ans=(c-wc)%3
        if ans==0:
            print("Carrots")
        elif ans==1:
            print("Kiwis")
        else:
            print("Grapes")
            
    