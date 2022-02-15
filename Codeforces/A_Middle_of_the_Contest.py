a = input().split(":")
b = input().split(":")
t1 = (int(a[0])+int(b[0]))
t2 = (int(a[1])+int(b[1]))
k = (60*t1+t2)//2
a = k//60
b = k%60
if a<10:
    a = "0"+str(a)
else:
    a = str(a)
if b<10:
    b = "0"+str(b)
else:
    b = str(b)
print(a+":"+b)