for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    if n%2==0:
        for i in range(0,n,2):
            print(l[i+1],-l[i],end=" ")
        print()
    else:
        temp=n-3
        for i in range(0,temp,2):
            print(l[i+1],-l[i],end=" ")
        if l[temp]+l[temp+1]!=0:
            print(l[temp+2],l[temp+2],-(l[temp]+l[temp+1]))
        elif l[temp]+l[temp+2]!=0:
            print(l[temp+1],-(l[temp]+l[temp+2]),l[temp+1])
        else:
            print(-(l[temp+1]+l[temp+2]),l[temp],l[temp])
        
            