# coding=utf-8
import sqlite3

banco = sqlite3.connect('surfersDB.sdb')
banco.row_factory = sqlite3.Row
cursor = banco.cursor()
cursor.execute('select * from surfers where age > 25')
linhas = cursor.fetchall()
for linha in linhas:
    print('Nome   :', linha['name'])
    print('País   :', linha['country'])
    print('Média  :', linha['average'])
    print('Estilo :', linha['board'])
    print('Idade  :', linha['age'])
    print()
cursor.close()
banco.close()
