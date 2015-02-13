# coding=utf-8
import random
lista = []
for x in range(10):
    numero = random.randint(1, 100)
    if x == 0:
        maior, menor = numero, numero
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    lista.append(numero)
lista.sort()
print(lista)
print("Maior: %d" % maior)
print("Menor: %d" % menor)
