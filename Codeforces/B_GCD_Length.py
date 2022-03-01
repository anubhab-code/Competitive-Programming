for _ in range(int(input())):
    a,b,c = map(int,input().split())
    a1,a2="1",""
    for i in range(a-1):
        a1+="0"
    for i in range(b-c+1):
        a2+="1"
    for i in range(c-1):
        a2+="0"
    print(a1,a2)