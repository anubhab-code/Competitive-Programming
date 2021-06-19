class List:
    def __init__(self, type):
        self.type = type
        self.items = []
        self.count = 0
    
    def add(self, item):
        if not isinstance(item, self.type):
            return "This item is not of type: {}".format(self.type.__name__)
        self.items.append(item)
        self.count += 1
        return self