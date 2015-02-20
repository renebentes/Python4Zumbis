# coding=utf-8
import string

arquivo = open('alice.txt')
texto = arquivo.read()
texto = texto.lower()
for c in string.punctuation:
    texto = texto.replace(c, '')
texto = texto.split()

dic = {}
for p in texto:
    if p not in dic:
        dic[p] = 1
    else:
        dic[p] += 1
print('Alice aparece %s vezes' % dic['alice'])
arquivo.close()
