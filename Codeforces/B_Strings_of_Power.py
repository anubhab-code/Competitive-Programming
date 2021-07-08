from bisect import bisect_left 
s=input()
heavy=[]
driver=[]
for i in range(len(s)):
    if i+5<=len(s):
        if s[i:i+5]=="heavy":
            heavy.append(i)
    if i+5<=len(s):
        if s[i:i+5]=="metal":
            driver.append(i)
ans=0
for j in heavy:
    x=bisect_left(driver,j)
    ans+=len(driver)-x
print(ans)