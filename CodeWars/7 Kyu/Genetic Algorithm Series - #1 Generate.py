import random

def generate(length):
    chromosome = [str(random.randint(0, 1)) for i in range(length)]
    return ''.join(chromosome)