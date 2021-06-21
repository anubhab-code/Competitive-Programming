n=int(input())
coins=list(map(int, input().split()))
total = 0
for i in coins:
    total += i
coins.sort(reverse=True)
mt = 0
count = 0
ht = total/2
for i in coins:
    if mt>ht:
        break
    mt+=i
    count+=1
print(count)