num = 'abcdefghijklmnopqrstuvwxyz'
def add_letters(*letters):
    x = 0
    x = sum(num.index(i)+1 for i in letters)
    while x-1 > 25:
        x -= 26
    return num[x-1]