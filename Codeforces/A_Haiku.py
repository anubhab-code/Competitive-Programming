s1=input()
s2=input()
s3=input()
count1=s1.count('a')+s1.count('e')+s1.count('i')+s1.count('o')+s1.count('u')
count2=s2.count('a')+s2.count('e')+s2.count('i')+s2.count('o')+s2.count('u')
count3=s3.count('a')+s3.count('e')+s3.count('i')+s3.count('o')+s3.count('u')
if count1==5 and count2==7 and count3==5: 
    print("YES")
else:
    print("NO")