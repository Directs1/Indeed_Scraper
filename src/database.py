
import sqlite3
print("SQLite3 version:", sqlite3.version)
print("SQLite3 is working!")

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)')
cursor.execute('INSERT INTO test (name) VALUES (?)', ('Test Job',))
result = cursor.fetchone()
conn.close()
print("Database operations working!")