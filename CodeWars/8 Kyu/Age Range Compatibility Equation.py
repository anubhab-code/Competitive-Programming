def dating_range(age):
    if age<=14:
        return str(int(age - 0.10 * age))+"-"+str(int(age + 0.10 * age))
    else:
        return str(int((age//2))+7)+"-"+str((age-7)*2)