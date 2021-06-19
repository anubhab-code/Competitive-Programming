def validate(username, password):
    return Database().login(username, password)