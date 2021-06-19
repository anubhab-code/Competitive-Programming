def caeser(message, key):
    x = list((map(ord,message)))
    def foo(a):
        if 96 < a < 123:
            if a + key < 123:
                return chr(a + key)
            else:
                return chr(a + key - 123 + 97)
        else:
             return chr(a)
    return ''.join(map(foo,x)).upper()