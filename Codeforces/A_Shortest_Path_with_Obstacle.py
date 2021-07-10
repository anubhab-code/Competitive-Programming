for _ in range(int(input())):
    a=input()
    xa,ya=map(int,input().split())
    xb,yb=map(int,input().split())
    xf,yf=map(int,input().split())
    if xa != xb and ya != yb:
        print(abs(xa-xb) + abs(ya-yb))
    else:
        if xa==xb:
            if xf == xa and yf>= min(ya,yb) and yf <= max(ya,yb):
                print(abs(ya-yb)+2)
            else:
                print(abs(ya-yb))
        elif ya==yb:
            if yf == ya and xf >= min(xa, xb) and xf <= max(xa, xb):
                print(abs(xa-xb)+2)
            else:
                print(abs(xa-xb))
