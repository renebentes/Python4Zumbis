a = int(input('Primeiro: '))
b = int(input('Segundo: '))
while (a % b != 0):
    a, b = b, a % b
print('MDC = %d' % b)
