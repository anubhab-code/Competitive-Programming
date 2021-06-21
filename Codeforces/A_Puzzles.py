s , p = list(map(int,input().split()))
data = sorted(list(map(int,input().split())))
min_ = 100000
for i in range(p-s+1):
    temp = data[i:i+s]
    if max(temp)-min(temp) < min_:
        min_ = max(temp) - min(temp)
print(min_)