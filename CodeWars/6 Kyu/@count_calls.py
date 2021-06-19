class count_calls():
    def __init__(self, func):
        self.func = func
        self.call_count = 0
        self.__name__ = func.__name__
        self.__doc__ = func.__doc__

    def __call__(self, *args, **kwargs):
        self.call_count += 1
        return self.func(*args, **kwargs)