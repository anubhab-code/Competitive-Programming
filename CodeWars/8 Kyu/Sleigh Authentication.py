class Sleigh(object):
    def authenticate(self, name, password):
        self.name, self.password = name, password
        return (self.name, self.password) == ('Santa Claus', 'Ho Ho Ho!')