import operator
def calculate(a, o, b):
    action = {"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.div} 
    try:
        return action[o](a,b)
    except:
        return None