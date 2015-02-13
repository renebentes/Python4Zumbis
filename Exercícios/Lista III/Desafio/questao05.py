'''
  Minha Solução
numero = int(input('Número Inteiro Positivo: '))
print('Número invertido: %d' %int(str(numero)[::-1]))
'''

'''
  Solução do Prof.
'''
numero = int(input('Número Inteiro Positivo: '))
inverso = 0
while numero > 0:
    inverso *= 10
    inverso += numero % 10
    numero //= 10
print('Número invertido: %d' % inverso)
