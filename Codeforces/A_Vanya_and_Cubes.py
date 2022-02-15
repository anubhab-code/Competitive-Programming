n = int(input())  
s1,s2 = 0,0  
i=1
while True:
    s1=(i*(i+1))//2
    s2+=s1
    if s2>n:
        print(i-1)
        break
    i+=1