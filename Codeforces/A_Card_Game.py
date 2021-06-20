t=input()
a,b=map(str,input().split())
l=["6", "7", "8", "9", "T", "J", "Q", "K" ,"A"]
if t in a :
    if t in b:
        if l.index(a[0])>l.index(b[0]):
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
    
else:
    if a[1]==b[1] and l.index(a[0])>l.index(b[0]):
        print("YES")
    else:
        print("NO")