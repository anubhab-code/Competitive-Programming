class Dictionary(dict):
    newentry = dict.__setitem__
    
    def look(self, key):
        return self.get(key, f"Can't find entry for {key}")