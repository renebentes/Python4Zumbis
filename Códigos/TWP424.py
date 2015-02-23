import urllib.request
import json

proxy = urllib.request.ProxyHandler(
    {'http': r'http://screne:#rmr08\@@10.89.136.250:3128'})
auth = urllib.request.HTTPBasicAuthHandler()
opener = urllib.request.build_opener(proxy, auth, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)

url = 'https://graph.facebook.com/renebpinto/friendlist?access_token=CAACEdEose0cBABBCeKRLTdYbe1XNnDhte8TQBtcJSd8NSUy2VcDzZBQDjCXcEIuMKHFwPSxrf7O9pSTbljySuDCae5EiZC66s9Iorbo9SZAv1ZArbeKHZAPAuaI4NnpV7pIhXCvVFzk4W3cnr4TsQ4EU1d1KzmPU2g1vSj6tz9hkNJOfncN0YL4eRwxdDUDtYZAPLAdYtBo6bZCTLUtrQBZCgEKr0mUg7ZCgZD'
resp = urllib.request.urlopen(url).read()
data = json.loads(resp.decode('utf-8'))
for amigo in data['data']:
    print(amigo['name'])
