for _ in range(int(input())):
    n,s=map(int,input().split())
    string=str(n)
    summ=0
    for i in string:
        summ+=int(i)
    if summ<=s:
        print(0)
        continue
    i=0
    summ=0
    while i<len(string) and summ+int(string[i])<s:
        summ+=int(string[i])
        i+=1
    diff=len(string)-i
    num=n%(pow(10,diff))
    print(pow(10,diff)-num)