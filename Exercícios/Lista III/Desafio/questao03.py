numero = int(input('Número: '))

x = 1
div = 0
while x <= numero:
    if numero % x == 0:
        div += 1
    if div > 2:
        break
    x += 1

if div == 2:
    print('%d é primo' % numero)
else:
    print('%d não é primo' % numero)
