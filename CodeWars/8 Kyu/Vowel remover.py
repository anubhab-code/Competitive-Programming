def shortcut(s):
    for i in ["a","e","i","o","u"]:
        if i in s:
            s = s.replace(i,"")

    return(s)