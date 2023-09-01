import psycopg2
from dotenv import dotenv_values
from argon2 import PasswordHasher
import os
import platform

config = dotenv_values(".env")

DB_NAME = config['DB_NAME']
DB_USER = config['DB_USER']
DB_PASS = config['DB_PASS']
DB_HOST = config['DB_HOST']
DB_PORT = config['DB_PORT']

PH = PasswordHasher()


def register(username: str, password: str):
    with conn.cursor() as cur:
        cur.execute("SELECT username FROM users WHERE username = %(username)s", {
                    'username': username
                    })
        result = cur.fetchone()

    if result is not None:
        print("[ERROR] Username already exists.")
    else:
        password = PH.hash(password)
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users(username, password) VALUES(%(username)s, %(password)s)", {
                'username': username,
                'password': password
            })
        print("[SUCCESS] User added to database.")


def verify(username: str, password: str):
    with conn.cursor() as cur:
        cur.execute("SELECT username FROM users WHERE username = %(username)s", {
                    'username': username
                    })
        result = cur.fetchone()

    if result is None:
        print("[ERROR] Username not found.")
    else:
        with conn.cursor() as cur:
            cur.execute("SELECT password FROM users WHERE username = %(username)s", {
                        'username': username
                        })
            result = cur.fetchone()

        if PH.verify(result[0], password):
            print("[SUCCESS] Username and password verified.")
        else:
            print("[ERROR] Invalid Password.")


if __name__ == "__main__":
    try:
        conn = psycopg2.connect(database=DB_NAME,
                                user=DB_USER,
                                password=DB_PASS,
                                host=DB_HOST,
                                port=DB_PORT)
        conn.set_session(autocommit=True)

        print("[SUCCESS] Database Connected.")

    except:
        print("[ERROR] Could not connect to database.")

    with conn.cursor() as cur:
        cur.execute("""CREATE TABLE IF NOT EXISTS users(
                        user_id SERIAL PRIMARY KEY, 
                        username VARCHAR(40) NOT NULL UNIQUE, 
                        password VARCHAR(200) NOT NULL
                    )""")

    if platform.system() == "Windows":
        os.system("cls")
    elif platform.system() in ["Linux", "Darwin"]:
        os.system("clear")

    while True:

        print("\n\nARGON2 + POSTGRESQL Test\n1.Verify\n2.Register\n3.Exit")
        choice = int(input("Choice: "))

        match choice:
            case 1:
                username = input("\nUsername: ")
                password = input("Password: ")
                verify(username, password)

            case 2:
                username = input("\nUsername: ")

                if not 1 <= len(username) <= 40:
                    print("[ERROR] Username length should be between 1-40")

                else:
                    password = input("Password: ")
                    password2 = input("Re-enter Password: ")

                    if password is not None and password == password2:
                        register(username, password)
                    else:
                        print("[ERROR] Passwords dont match / Invalid password.")

            case 3:
                break
