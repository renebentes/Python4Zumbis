# coding=utf-8
'''
  Minha Solução
cripto = ''
with open('mensagem.txt') as f:
    linha = f.read()
    for x in range(len(linha)):
        if linha[x] in 'aeiou':
            cripto += '*'
        else:
            cripto += linha[x]
with open('cripto.txt', 'w') as c:
    c.write(cripto)
'''
'''
  Solução do Prof.
'''
texto = open('mensagem.txt')
saida = open('cripto.txt', 'w')
for linha in texto.readlines():
    for letra in linha:
        if letra in 'aeiou':
            saida.write('*')
        else:
            saida.write(letra)
texto.close()
saida.close()
