def get_first_python(users):
    for list in users:
        if list [ 'language' ] == 'Python':
            return list [ 'first_name' ] + ', ' + list [ 'country' ]
    return 'There will be no Python developers'