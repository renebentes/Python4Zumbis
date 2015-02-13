valor = float(input('Valor da hora: R$ '))
hora = int(input('Horas trabalhadas: '))

bruto = valor * hora
ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05

print('+ Salário Bruto: R$%10.2f' % bruto)
print('- IR: R$%10.2f' % ir)
print('- INSS: R$%10.2f' % inss)
print('- Sindicato: R$%10.2f' % sindicato)
print('= Salário Líquido: R$%10.2f' % (bruto - ir - inss - sindicato))
