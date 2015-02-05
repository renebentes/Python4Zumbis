dias = int(input('Digite o número de dias: '))
horas = int(input('Digite o número de horas: '))
minutos = int(input('Digite o número de minutos: '))
segundos = int(input('Digite o número de segundos: '))

result = 0
result = result + dias * 86400
result = result + horas * 3600
result = result + minutos * 60
result = result + segundos

print('%d dias, %d horas, %d minutos e %d segundos = %d segundos' %
      (dias, horas, minutos, segundos, result))
