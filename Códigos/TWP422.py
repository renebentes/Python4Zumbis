import urllib.request

proxy = urllib.request.ProxyHandler(
    {'http': r'http://***:***@1.1.1.1:3128'})
auth = urllib.request.HTTPBasicAuthHandler()
opener = urllib.request.build_opener(proxy, auth, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)

user = 'renebpinto'
url = 'https://graph.facebook.com/' + user + '/picture?type=large'
resp = urllib.request.urlopen(url).read()

f = open(user + '.jpg', 'wb')
f.write(resp)
f.close()

print(user + '.jpg', 'gravado no disco')
