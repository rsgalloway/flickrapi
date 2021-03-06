import sys
import requests
from requests_oauthlib import OAuth1
import urllib

url = "http://www.flickr.com/services/oauth/request_token"

key = "a233c66549c9fb5e40a68c1ae156b370"
secret = "03fbb3ea705fe096"

queryoauth = OAuth1(key, secret, signature_type='query')

params = {
    'oauth_callback': 'http://localhost:8080/'
}

r = requests.get(url,
                 auth=queryoauth,
                 params=params,
                 )

assert isinstance(r, requests.Response)

print(50 * '-')
print(r.status_code)
print(r.text)
print(50 * '-')

parts = r.text.split('&')
for part in parts:
    print(urllib.unquote(part))
print(50 * '-')
