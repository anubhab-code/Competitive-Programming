def make_lazy(func, *args):
    def new_fun():
      return func(*args)
    return new_fun