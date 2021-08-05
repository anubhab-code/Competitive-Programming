for _ in range(int(input())):
    l,r=map(int,input().split(" "))
    rlist=[int(x) for x in bin(r)[2:]]
    llist=[int(x) for x in bin(l)[2:]]
    llist=llist[::-1]
    cnt=sum(llist)
    for i in range(len(rlist)):
        if i>=len(llist):
            if l+2**i<=r:
                l+=2**i
                cnt+=1
        elif llist[i]==0:
            if l+2**i<=r:
                l+=2**i
                cnt+=1
    print(l)