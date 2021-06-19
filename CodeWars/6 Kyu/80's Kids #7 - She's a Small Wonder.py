class Robot:
    def __init__(self): 
        self.vocabulary = 'Thank you for teaching me I do not understand the input already know word'.lower().split(' ')
    
    def learn_word(self, word): 
        if not word.isalpha(): return 'I do not understand the input'
        if word.lower() in self.vocabulary: return 'I already know the word {}'.format(word)
        self.vocabulary.append(word.lower())
        return 'Thank you for teaching me {}'.format(word) 