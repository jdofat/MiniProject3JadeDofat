# SQLite import, database connection, start the setup, create tables (users: id, email, pass) and meals (id, user id, meal, cals), and save changes/close connection

import sqlite3

# connects to the database file-
def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn

# builds 2 tables (users & meals)-
def init_db():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT, password TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS meals (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, meal TEXT, calories INTEGER, FOREIGN KEY (user_id) REFERENCES users (id))')

    conn.commit()
    conn.close()
