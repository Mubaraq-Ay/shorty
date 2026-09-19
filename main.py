import urllib.parse

user_url = input('Enter url: ')

parsed = urllib.parse.urlparse(user_url)

if parsed.scheme in ['http', 'https'] and parsed.netloc:
    print('pass')
else:
    print('fail')
