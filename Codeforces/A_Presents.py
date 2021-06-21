n = int(input())
data = list(map(int,input().split()))
d = {}
for i in range(len(data)):
    d[data[i]] = i+1
for i in range(1,len(data)+1):
    print(d[i],end=' ')