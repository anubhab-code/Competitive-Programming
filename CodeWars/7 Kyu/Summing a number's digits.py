def sumDigits(number):
    number = abs(number)
    return_number = 0
    
    while number > 0:
        return_number += number % 10
        number = int(number / 10)
        
    return return_number