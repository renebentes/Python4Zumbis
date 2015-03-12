# coding: utf-8
import urllib.request

proxy = urllib.request.ProxyHandler(
    {'http': r'http://****:****@1.1.1.1:3128'})
auth = urllib.request.HTTPBasicAuthHandler()
opener = urllib.request.build_opener(proxy, auth, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)

pagina = urllib.request.urlopen('http://beans.itcarlow.ie/prices-loyalty.html')
texto = pagina.read().decode('utf8')
onde = texto.find('>$')
inicio = onde + 2
fim = inicio + 4
preco = texto[inicio:fim]
if preco < 4.74:
    print(preco)
