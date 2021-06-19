def generate_link(user):
    user = ''.join(('%'+hex(ord(let)).upper()[-2:] if not (let.isalpha() or let.isdigit() or let == '_' or let == '.' or let == '/') else let) for let in user)
    return 'http://www.codewars.com/users/'+user