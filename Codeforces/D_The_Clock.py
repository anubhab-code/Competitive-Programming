for _ in range(int(input())):
    s,d = input().split()
    d = int(d)
    h,m = map(int, s.split(':'))
    ans = 0
    f = set()
    while (h, m) not in f:
        # print(h,m)
        f.add((h,m))
        m += d
        h += m//60
        m %= 60
        h %= 24
        check = f'{str(h).zfill(2)}:{str(m).zfill(2)}'
        if check == check[::-1]:
            ans += 1
    print(ans)