# coding: utf-8
import sqlite3

con = sqlite3.connect('alunos.sdb')
cursor = con.cursor()
cursor.execute('create table alunos(login varchar(8), ra integer)')
cursor.close()
con.close()
