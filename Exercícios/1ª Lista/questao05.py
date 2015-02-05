preco = int(input('Informe o preço do produto: '))
desconto = int(input('Informe a porcentagem de desconto: '))

totaldesconto = preco * (desconto / 100)

print('Valor do desconto: R$ %10.2f' % (totaldesconto))
print('Valor do produto: R$ %10.2f' % (preco - totaldesconto))
