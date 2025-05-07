import sqlite3

conn = sqlite3.connect("your_database_file.db")  # Replace with your actual file
cursor = conn.cursor()

# View all users
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

# Print each user
for user in users:
    user_id, username, password = user
    print(f"ID: {user_id}, Username: {username}, Password: {password}")

conn.close()