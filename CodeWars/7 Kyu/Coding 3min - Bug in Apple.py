def sc(apple):
    for i in apple:
        if 'B' in i:
            return [apple.index(i), i.index('B')]