from operator import mul,add,div,sub
operators = {'add':add, 'subtract':sub, 'multiply':mul }
def calculate(n1, n2, o):    
    return '{:b}'.format(operators[o](int(n1,2), int(n2,2)))