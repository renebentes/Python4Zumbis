palavra = input('Palavra: ')
texto = ''
x = 0

while x < len(palavra):
    if palavra[x] in 'aeiou':
        texto = texto + '*'
    else:
        texto = texto + palavra[x]
    x += 1
print(texto)
