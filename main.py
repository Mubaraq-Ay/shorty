import urllib.parse

user_url = input('Enter url: ')

parsed = urllib.parse.urlparse(user_url)

if parsed.scheme and parsed.netloc:
    print('j')
else:
    print('jjj')
 