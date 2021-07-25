n = int(input())
data = [1,2,6,24,120,720,5040,40320,362880,3628800]
coins = 0
for i in range(9,-1,-1):
    if n == 0:
        break
    if n >= data[i]:
        coins += n//data[i]
        n = n%data[i]
print(coins)