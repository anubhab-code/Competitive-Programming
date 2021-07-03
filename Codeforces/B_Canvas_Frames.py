from typing import Counter
n = int(input())
l = list(map(int,input().strip().split()))[:n]
print(sum(val//2 for val in Counter(l).values())//2)