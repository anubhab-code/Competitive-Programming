def filter_long_words(sentence,long):
    return [word for word in sentence.split() if len(word) > long]