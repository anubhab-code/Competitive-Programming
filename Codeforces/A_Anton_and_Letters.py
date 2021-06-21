string = input()[1:-1].split(',')
if string == ['']:
    print(0)
else:
    print(len(set([x.strip() for x in string])))