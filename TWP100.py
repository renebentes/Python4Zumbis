vel = int(input('Informe a velocidade: '))

if vel > 110:
    print('Você foi multado!')
    multa = (vel - 110) * 5
    print('Valor da multa: R$ %5.2f' % multa)
