# coding=utf-8
def inteirosdistintos():
    import random
    inteiros = []
    while len(inteiros) < 15:
        x = random.randint(10, 100)
        if x not in inteiros:
            inteiros.append(x)
    return inteiros
