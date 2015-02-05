minutes = int(input('Minutos usados: '))
if minutes < 200:
    price = 0.20
else:
    if minutes <= 400:
        price = 0.18
    else:
        if minutes <= 800:
            price = 0.15
        else:
            price = 0.08
print('Sua conta é: R$ %6.2f' % (minutes * price))
