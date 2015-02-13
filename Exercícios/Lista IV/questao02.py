# coding=utf-8
import random
lista, par, impar = [], [], []
for x in range(20):
    numero = random.randint(1, 100)
    lista.append(numero)
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
print(lista)
print(par)
print(impar)
