# coding=utf-8
f = open('surf.txt')
notas = []
for linha in f:
    nomes, pontos = linha.split()
    notas.append(float(pontos))
f.close()
notas.sort()
notas.reverse()
# notas.sort(reverse=True)
print(notas[0])
print(notas[1])
print(notas[2])
