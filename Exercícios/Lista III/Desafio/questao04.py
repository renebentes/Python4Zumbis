'''
  Minha Solução
numero = int(input('Número: '))
fator = 2
vetor = []
x = 0

fator = 2
while (numero > 1):
  mult = 0
  while numero % fator == 0:
    mult += 1
    print("%d\t| %d" %(numero, fator))
    numero = numero / fator;
  if mult != 0:
    vetor.append("fator %d multiplicidade %d" %(fator, mult))
  fator += 1
print("%d\t| " %numero)
while x < len(vetor):
  print(vetor[x])
  x += 1
'''

'''
  Soluçãod do Prof
'''
numero = int(input('Número: '))
for k in range(2, numero):
    while numero % k == 0:
        print(k)
        numero = numero / k
