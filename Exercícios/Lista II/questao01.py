print('Informe um valor para os 3 lados de um triângulo.')
a = int(input('Informe um valor para o 1º lado: '))
b = int(input('Informe um valor para o 2º lado: '))
c = int(input('Informe um valor para o 3º lado: '))

if a < b + c and b < a + c and c < a + b:
    print('Os valores formam um triângulo.')
    if a == b == c:
        print('Equilátero.')
    elif a == b or a == c or b == c:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print(
        'Os valores não formam um triângulo. Pelo menos um dos valores é maior que a soma dos outros dois.')
