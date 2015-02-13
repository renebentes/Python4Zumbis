km = int(input('Informe a quilometragem percorrida: '))
dias = int(input('Informe quantos dias de aluguel: '))

print('Total a pagar pelo carro: R$%6.2f' % (dias * 60 + km * 0.15))
