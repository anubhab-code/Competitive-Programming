for _ in range(int(input())):
    n=int(input())
    s=input()
    if n%2!=0:
        if s.count('0')>1:
            if s[n//2]=='0':
                print('ALICE')
                continue
    print('BOB')