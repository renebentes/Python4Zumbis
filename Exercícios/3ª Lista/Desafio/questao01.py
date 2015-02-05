'''
  Minha Solução
num = int(input('Número: '))
x = 1
prod = 1
resp = False
while prod <= num:
  prod = x * (x + 1) * (x + 2)
  if prod == num:
    resp = True
  x += 1
if resp == True:
  print('%d x %d x %d = %d, logo é um número triangular'
    %((x - 2), (x - 1), x, num))
else:
  print('%d não é um número triangular' %num)
'''

'''
  Solução do Prof
'''
num = int(input('Número: '))
k = 0
while k * (k + 1) * (k + 2) < num:
    k += 1
if k * (k + 1) * (k + 2) == num:
    print('Triangular')
else:
    print('Não triangular')
