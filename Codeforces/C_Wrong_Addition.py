for _ in range(int(input())):
    a,b = map(str,input().split())
    l1 = len(a)
    l2 = len(b)
    flag = True
    k = ""
    while l1>0 and l2>0:
        if a[-1]<=b[-1]:
            l1-=1
            l2-=1
            a1 = a[-1]
            b1 = b[-1]
            a = a[:-1]
            b = b[:-1]
            a1 = int(a1)
            b1 = int(b1)
            if not (b1-a1 <10):
                flag = False
                break
            else:
                k = f"{b1-a1}" + k
            
        else:
            l1-=1
            l2-=2
            if l2>=0:
                pass
            if l2<0:
                flag = False
                break
            a1 = a[-1]
            b1 = b[-2:]
            a = a[:-1]
            b = b[:-2]
            a1 = int(a1)
            b1 = int(b1)
            if not (b1-a1 <10 and b1-a1>=0):
                flag = False
                break
            else:
                k = f"{b1-a1}" + k
    if not (l1 or not flag):
        print(int(b+k))
    else:
        print(-1)
        