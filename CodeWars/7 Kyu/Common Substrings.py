def substring_test(str1, str2):
    for n in xrange(len(str2)-1):
        if str2[n:n+2].lower() in str1.lower():
            return True
    return False