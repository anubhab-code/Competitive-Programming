import re
def AlphaNum_NumAlpha(string):
    r=''
    for m in re.findall(r'(\d+|[a-z])',string):
        if m.isdigit():
            r+=alphabet[int(m)-1]
        else:
            r+=alphabetnums[m]
    return r