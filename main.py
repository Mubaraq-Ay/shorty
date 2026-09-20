import urllib.parse
import secrets
import sqlite3

print("""
----- SHORTY -----

Select an option:

1. Shorten URL
2. Exit
""")

choice = input("Select an option: ")

if choice == "1":

    while True:
        user_url = input("Enter URL: ")
        parsed = urllib.parse.urlparse(user_url)

        if parsed.scheme in ['http', 'https'] and parsed.netloc:
            break

        print("Invalid URL, kindly enter a valid one.")


    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    def generate_code():
        char = []

        for _ in range(6):
            random_str = secrets.choice(characters)
            char.append(random_str)

        short_code = ''.join(char)
        return short_code


    conn = sqlite3.connect('url.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls(
            original_url TEXT,
            short_code TEXT
        )
    """)

    conn.commit()

    while True:
        short_code = generate_code()

        cursor.execute("""
            SELECT * FROM urls
            WHERE short_code = ?;
        """, (short_code,))

        result = cursor.fetchone()

        if result is not None:
            continue

        break

    cursor.execute("""
        INSERT INTO urls(original_url, short_code)
        VALUES (?, ?)
    """, (user_url, short_code))

    conn.commit()
 
    print(short_code)

elif choice == "2":
    print("Okay, bye.")

else:
    print("Invalid option.")
