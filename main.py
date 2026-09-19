import urllib.parse
import secrets
import sqlite3

while True:
    user_url = input('Enter url: ')
    parsed = urllib.parse.urlparse(user_url)
    if parsed.scheme in ['http', 'https'] and parsed.netloc:
        break
    else:
        print('Invalid URL, kindly enter a valid one.')

         
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
char = []

for _ in range(6):
    random_str = secrets.choice(characters)
    char.append(random_str)

rs = ''.join(char)
print(rs)

 

