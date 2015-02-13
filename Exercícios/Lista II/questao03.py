peso = float(input('Informe o peso dos peixes: '))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    multa = 0
    excesso = 0

print('Peso total de Peixes: %5.2f' % peso)
print('Excesso de Peso: %5.2f' % excesso)
print('Multa: R$ %5.2f' % multa)
