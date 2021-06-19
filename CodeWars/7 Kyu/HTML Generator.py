class HTMLGen(object):
    def __getattr__(self, name):
        def wrapper(text):
            if name == "comment":
                return "<!--{0}-->".format(text)
            else:
                return "<{0}>{1}</{0}>".format(name, text)
        return wrapper