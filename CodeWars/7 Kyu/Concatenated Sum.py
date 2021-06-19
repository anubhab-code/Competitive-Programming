def check_concatenated_sum(original,n):
    check = []
    try:
        for i in str(abs(original)):
            check.append(i*n)
        check = list(map(int,check))
        return sum(check) == abs(original)
    except:
        return False