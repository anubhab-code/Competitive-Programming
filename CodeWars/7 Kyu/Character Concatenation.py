def char_concat(word):
    string = ''
    for i in range(int(len(word)/2)):
        string += word[i] + word[-i-1] + str(i+1)
    return string