area = float(input('Área de pintura (m²): '))

if area % 54 == 0:
    lata = area / 54
else:
    lata = int(area / 54) + 1

print('Latas: %d' % lata)
print('Valor Total: R$%5.2f' % (lata * 80))
