n = int(input('Informe um número para calcular o fatorial: '))
x = 1
fatorial = 1
while x <= n:
    fatorial = fatorial * x
    x = x + 1
print('Fat(%d) = %d' % (n, fatorial))
