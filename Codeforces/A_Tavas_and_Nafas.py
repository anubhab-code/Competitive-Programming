x = int(input())

a = ['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen',
     'fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
b = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
 
print(a[x] if x < 20 else b[x//10-2] + ('' if x % 10==0 else '-'+a[x%10]))