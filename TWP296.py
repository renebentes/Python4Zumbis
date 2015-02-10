# coding=utf-8
def inteirosrandom():
    import random
    inteiros = []
    for x in range(15):
        inteiros.append(random.randint(10, 100))
    return inteiros
