string = input().lower()
new = ''
for i in string:
    if i not in ['a','e','i','o','u','y']:
        new += '.'+i
print(''.join(new))