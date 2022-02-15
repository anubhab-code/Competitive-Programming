n = int(input())
s = input()
k,i = 0,0
while k<n:
    print(s[k],end='')
    for j in range(i+1):
        k+=1
    i+=1