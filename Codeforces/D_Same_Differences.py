from collections import Counter
for i in range(int(input())):
    count=0
    num=int(input())
    given=list(map(int,input().split()))
    for j in range(len(given)):
        given[j]=given[j]-j
    dictionary=Counter(given)
    for f in dictionary.values():
        count = count + (((f**2)-f)/2)
    final=int(count)
    print(final)