'''
  Minha solução

conta = float(input('Valor da Conta: '))
pago = float(input('Valor Pago: '))

notas = [0, 0, 0, 0, 0, 0]

if pago >= conta:
  troco = int(pago - conta)
  print('O troco de %d pode ser distribuído da seguinte forma:' %troco)

  while troco > 0:
    if troco >= 50:
      troco -= 50
      notas[5] += 1
    elif troco >= 20:
      troco -= 20
      notas[4] += 1
    elif troco >= 10:
      troco -= 10
      notas[3] += 1
    elif troco >= 5:
      troco -= 5
      notas[2] += 1
    elif troco >= 2:
      troco -= 2
      notas[1] += 1
    else:
      troco -=1
      notas[0] += 1

  print('Notas de 50:\t%d' %notas[5])
  print('Notas de 20:\t%d' %notas[4])
  print('Notas de 10:\t%d' %notas[3])
  print('Notas de 5:\t%d' %notas[2])
  print('Notas de 2:\t%d' %notas[1])
  print('Notas de 1:\t%d' %notas[0])
else:
  print('Você ainda está devendo')
'''

'''
  Solução do Prof.
'''
conta = int(input('Valor da Conta: '))
pago = int(input('Valor Pago: '))
troco = pago - conta
notas = [50, 20, 10, 5, 2, 1]
for nota in notas:
    while troco >= nota:
        print('Uma nota de %d' % nota)
        troco -= nota
