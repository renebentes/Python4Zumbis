salario = int(input('Informe o salário: '))
aumento = int(input('Informe a porcentagem de aumento: '))

totalaumento = salario * (aumento / 100)
print('Valor do aumento: R$ %10.2f' % (totalaumento))
print('Valor do novo salário: R$ %10.2f' % (salario + totalaumento))
