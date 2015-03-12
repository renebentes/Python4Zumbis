# coding: utf-8
import urllib.request
import json

proxy = urllib.request.ProxyHandler(
    {'http': r'http://***:***@1.1.1.1:3128'})
auth = urllib.request.HTTPBasicAuthHandler()
opener = urllib.request.build_opener(
    proxy, auth, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
url = 'http://api.icndb.com/jokes/random?limitTo=[nerdy]'

resp = urllib.request.urlopen(url).read()
data = json.loads(resp.decode('utf-8'))

print(data['value']['joke'])
