# coding=utf-8
from random import randint

sorteado = randint(1, 100)

while True:
    chute = int(input("Chute um número: "))
    if chute == sorteado:
        print("Parabéns! Você acertou o número %d" % sorteado)
        break
    else:
        print('Alto' if chute > sorteado else 'Baixo')

print('Fim de Jogo')
