a = int(input('Informe o 1º valor: '))
b = int(input('Informe o 2º valor: '))
c = int(input('Informe o 3º valor: '))

if a >= b and a >= c:
    print('Maior valor %d.' % a)
elif b >= c:
    print('Maior valor %d.' % b)
else:
    print('Maior valor %d.' % c)

if a <= b and a <= c:
    print('Menor valor %d.' % a)
elif b <= c:
    print('Menor valor %d.' % b)
else:
    print('Menor valor %d.' % c)
