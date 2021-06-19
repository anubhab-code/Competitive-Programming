def openOrSenior(data):
    return ['Senior' if age >= 55 and h > 7 else 'Open' for age, h in data]