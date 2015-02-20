'''
  Solução I
data = input('Data: ')
meses = ['', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
data = data.split('/')

print('%s de %s de %s' %(data[0], meses[int(data[1])], data[2]))
'''

'''
  Solução II
'''
dia, mes, ano = input('Data: ').split('/')
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
print('Voçê nasceu em %s de %s de %s' % (dia, meses[int(mes) - 1], ano))
