n = int(input())
l = list(map(int,input().split()))
t = l
t=sorted(t)
for i in range(n-1):
    if l[i] > l[i+1]:
        start = i
        end = i+1
        while end < n:
            if l[end-1] > l[end]:
                end += 1
            else:
                break
        new = l[start:end][::-1]
        l[start:end] = new
        if l == t:
            print("yes")
            print(start+1,end)
            break
        print("no")
        break
    else:
        print("yes")
        print(1,1)
        break