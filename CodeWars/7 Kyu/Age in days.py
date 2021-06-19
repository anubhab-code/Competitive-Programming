from datetime import date

def ageInDays(y, m, d):
    return f"You are {(date.today() - date(y, m, d)).days} days old"
    