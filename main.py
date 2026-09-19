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

short_code = ''.join(char)
print(short_code)

conn = sqlite3.connect('url.db')
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS urls(
        original_url TEXT,
        short_code TEXT
    )
""")

conn.commit()

cursor.execute("""
    INSERT INTO urls(original_url, short_code)
    VALUES (?, ?)
""", (user_url, short_code))

conn.commit()

cursor.execute("""
    SELECT * FROM urls 
    WHERE short_code = ?;
""", (short_code,))

result = cursor.fetchone()
print(result)

