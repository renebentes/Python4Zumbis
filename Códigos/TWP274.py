letras = []
soma = x = 0

'''
  Método tradicional

while x < 10:
  letras.append(input('Letra: '))
  if letras[x] == 'b' or letras[x] == 'c' or letras[x] == 'd'
  or letras[x] == 'f' or letras[x] == 'g' or letras[x] == 'h'
  or letras[x] == 'j' or letras[x] == 'k' or letras[x] == 'l'
  or letras[x] == 'm' or letras[x] == 'n' or letras[x] == 'p'
  or letras[x] == 'q' or letras[x] == 'r' or letras[x] == 's'
  or letras[x] == 't' or letras[x] == 'v' or letras[x] == 'w'
  or letras[x] == 'x' or letras[x] == 'y' or letras[x] == 'z':
    soma += 1
  x += 1
'''
'''
  Método Otimizado Python
'''
while x < 10:
    letras.append(input('Letra: '))
    if letras[x] not in 'aeiou':
        soma += 1
    x += 1

print('Letras: %s' % letras)
print('Consoantes: %d' % soma)
