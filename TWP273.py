nota = []
soma = x = 0
while x < 4:
    nota.append(float(input('Nota: ')))
    soma += nota[x]
    x += 1
media = soma / x

print('Nota: %.2f' % nota)
print('Média: %.2f' % media)
