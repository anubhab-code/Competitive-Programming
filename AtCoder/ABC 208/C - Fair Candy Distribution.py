n,k = list(map(int,input().split()))
data = list(map(int,input().split()))
common = k // n
k = k % n
d = {}
for i in data:
    d[i] = False   
new_data = sorted(data)
for i in new_data[0:k]:
    d[i] = True
for i in data:
    if d[i] == True:
        print(common + 1)
    else:
        print(common)