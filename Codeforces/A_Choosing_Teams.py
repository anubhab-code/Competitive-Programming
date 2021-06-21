n,k = list(map(int,input().split()))
data = list(map(int,input().split()))
count = 0
for i in data:
    if i <= 5-k:
        count+=1
print(count//3)