# coding: utf-8
def fatorial(numero):
    fatorial = 1
    for x in range(1, numero):
        fatorial = fatorial * x
    print('Fat(%d) = %d' % (numero, fatorial))
