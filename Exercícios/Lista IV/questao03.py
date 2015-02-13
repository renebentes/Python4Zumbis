# coding=utf-8
import random
lista1, lista2, lista = [], [], []
for x in range(10):
    valor1 = random.randint(1, 100)
    lista1.append(valor1)
    lista.append(valor1)
    valor2 = random.randint(1, 100)
    lista2.append(valor2)
    lista.append(valor2)
print(lista1)
print(lista2)
print(lista)
