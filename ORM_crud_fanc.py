import sqlite3
import asyncio

def initiate_db():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    )
    '''),
    connection.commit()

initiate_db()

def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()
    products=cursor.execute('SELECT * FROM Products').fetchall()
    connection.commit()
    return products

connection = sqlite3.connect('Users.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INT PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INT NOT NULL,
balance INT NOT NULL
)
'''),
connection.commit()

def add_user(username, email, age):
    conn = sqlite3.connect('Users.db')
    cursor = conn.cursor()

    cursor.execute('''
    INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, 1000)
    ''', (username, email, age))

    conn.commit()
    conn.close()

def is_included(username):
    conn = sqlite3.connect('Users.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    user = cursor.fetchone()

    conn.close()
    return user is not None

connection.commit()
connection.close()