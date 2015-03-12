# coding:utf-8
import sqlite3

con = sqlite3.connect('alunos.sdb')
cursor = con.cursor()

cursor.execute('insert into alunos values(\'massanori\', 42)')
cursor.execute('insert into alunos values(\'emengarda\', 666)')
cursor.execute('select * from alunos')
for l in cursor.fetchall():
    print(l)
cursor.close()
con.commit()
con.close()
