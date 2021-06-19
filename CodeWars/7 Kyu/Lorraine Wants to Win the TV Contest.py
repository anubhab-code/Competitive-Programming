def unscramble(scramble):
    return [i for i in word_list if sorted(i) == sorted(scramble)]