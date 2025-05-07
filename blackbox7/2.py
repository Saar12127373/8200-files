import sqlite3

# Connect to your existing database
conn = sqlite3.connect("game_database.db")
cursor = conn.cursor()

# Insert one user
username = "admin"
password = "hunter2"  # Change this to whatever password you'd like

cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

# Save changes
conn.commit()
print(f"User '{username}' added successfully.")

conn.close()