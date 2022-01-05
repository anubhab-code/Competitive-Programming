def check(t1,t2,c):
    if t1!=t2:
        return c[t1]+c[t2]
    else:
        return c[t1]
 
for _ in range(int(input())):
    n = int(input())
    l,r,c = [0]*n,[0]*n,[0]*n
    for i in range(n):
        x,y,z = map(int,input().split())
        l[i] = x
        r[i] = y
        c[i] = z
    t1,t2,t3 = 0,0,0
    for i in range(n):
        if l[i]<l[t1] or (l[i]==l[t1] and c[i]<c[t1]):
            t1 = i
        if r[i]>r[t2] or (r[i]==r[t2] and c[i]<c[t2]):
            t2 = i
        if l[i]<l[t3] or r[i]>r[t3] or (l[i]==l[t3] and r[i]==r[t3] and c[i]<c[t3]):
            t3 = i
        # if t1!=t2:
        #     print(c[t1]+c[t2])
        # else:
        #     print(c[t1])
        # print(check(t1,t2,c))
        if l[t3] <= l[t1] and r[t3] >= r[t2] and (l[t3] < l[t1] or r[t3] > r[t2] or c[t3] < check(t1,t2,c)):
            print(c[t3])
        else:
            print(check(t1,t2,c))