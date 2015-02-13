'''
  Minha Solução
n = int(input('Número: '))
f = [1, 1]
cont = 2
while (cont < n):
  f.append(f[cont - 2] + f[cont - 1])
  cont += 1
print(f[n-1])
'''

'''
  Solução do Prof.
'''
n = int(input('Número: '))
a, b = 1, 1
k = 1

while k <= n - 2:
    a, b = b, a + b
    k += 1
print('F(%d) = %d' % (n, b))
