def alias_gen(f_name, l_name):
    if (not f_name[0].isalpha() or not l_name[0].isalpha()):
        return 'Your name must start with a letter from A - Z.'
    return FIRST_NAME.get(f_name[0].upper()) + " " + SURNAME.get(l_name[0].upper())