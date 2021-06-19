def _if(bool, func, func2):
    func() if bool else func2()
    
def truthy():
    print('True')
    
def falsey():
    print('False')