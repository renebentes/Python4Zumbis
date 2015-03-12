# coding: utf-8
def embaralha(string):
    import random
    lista = list(string)
    random.shuffle(lista)
    return ' '.join(lista)
