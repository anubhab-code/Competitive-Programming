x1, y1, x2, y2 = list(map(int, input().split()))
x3, y3, x4, y4 = list(map(int, input().split()))
x5, y5, x6, y6 = list(map(int, input().split()))

def check(x,y):
    return not ((x >= x3 and x <= x4 and y >= y3 and y <= y4) or (x >= x5 and x <= x6 and y >= y5 and y <= y6))
 
flag=False
diff=2*(x2-x1+1)
 
for i in range(diff-1):
   flag=flag or check(x1+0.5*i,y1)
diff=2*(x2-x1+1)
for i in range(diff-1):
   flag=flag or check(x1+0.5*i,y2)
diff=2*(y2-y1+1)
for i in range(diff-1):
   flag=flag or check(x1,i*0.5+y1)
diff=2*(y2-y1+1)
for i in range(diff-1):
   flag=flag or check(x2,i*0.5+y1)
 
if flag==False:
    print("NO")
else:
    print("YES")