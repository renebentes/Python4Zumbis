cigarro = int(input('Informe quantos cigarros por dia: '))
ano = int(input('Informe quantos anos fumando: '))

print('Você teve uma redução de %5.2f dias em sua vida' %
      (cigarro * 10 / 1440 * ano))
