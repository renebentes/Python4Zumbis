# coding=utf-8
import urllib.request
import time

proxy = urllib.request.ProxyHandler(
    {'http': r'http://*****:****@1.1.1.1:3128'})
auth = urllib.request.HTTPBasicAuthHandler()
opener = urllib.request.build_opener(proxy, auth, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)

preco = 99.99
while preco >= 4.74:
    pagina = urllib.request.urlopen(
        'http://beans.itcarlow.ie/prices-loyalty.html')
    texto = pagina.read().decode('utf8')
    onde = texto.find('>$')
    inicio = onde + 2
    fim = inicio + 4
    preco = float(texto[inicio:fim])
    if preco >= 4.74:
        time.sleep(600)
print(preco)
