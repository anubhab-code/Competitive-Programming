for _ in range(int(input())):
    w,h = map(int,input().split())
    l1 = list(map(int,input().split()))[1:]
    l2 = list(map(int,input().split()))[1:]
    l3 = list(map(int,input().split()))[1:]
    l4 = list(map(int,input().split()))[1:]
    mi1 = min(l1)
    mi2 = min(l2)
    mi3 = min(l3)
    mi4 = min(l4)
    ma1 = max(l1)
    ma2 = max(l2)
    ma3 = max(l3)
    ma4 = max(l4)
    ans=[]
    ans.append(abs(ma2-mi2)*h)
    ans.append(abs(ma3-mi3)*w)
    ans.append(abs(ma4-mi4)*w)
    ans.append(abs(ma1-mi1)*h)
    print(max(ans))
    