n,s=map(int,input().split())
cm=0
for i in range(n):
    fi,ti=map(int,input().split())
    if i==0:
        cm=fi+ti
    if i!=0:
        if fi+ti>cm:
            cm=fi+ti
if cm>s:
    print(cm)
else:
    print(s)