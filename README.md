# Argon2 Password Hashing with Python and PostgreSQL

Simple implementation for safely storing passwords in a PostgreSQL database

### Setup

Download or clone this repository

```cmd
git clone https://github.com/d0076/argon2-postgres-python.git
```

Install the required dependencies

```cmd
pip install -r requirements.txt
```

Setup the .env file with your PostgreSQL credentials

```sh
# REPLACE THE VALUES WITH YOUR OWN
DB_NAME="your_db_name"
DB_USER="your_db_user"
DB_PASS="your_db_password"
DB_HOST="your_db_host"
DB_PORT="your_db_port"
```

Run the program

> The program automatically creates a 'users' table

```cmd
python argon2-postgres.py
```

> You can customize the program to suit your needs.

## Resources

| Resource                  | Link                                          |
| ------------------------- | --------------------------------------------- |
| PostgreSQL Documentation  | https://www.postgresql.org/docs/              |
| Psycopg Documentation     | https://www.psycopg.org/docs/                 |
| argon2-cffi Documentation | https://argon2-cffi.readthedocs.io/en/stable/ |
| dotenv Documentation      | https://pypi.org/project/python-dotenv/       |
