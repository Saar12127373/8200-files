import sqlite3

conn = sqlite3.connect("game_database.db")
cursor = conn.cursor()

username = "lala"
password = "trting"  # Change this to whatever password you'd like

cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

conn.close()