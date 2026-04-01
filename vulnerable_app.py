import subprocess
import sqlite3
import hashlib

username = input("Enter username: ")
password = input("Enter password: ")

# SQL Injection vulnerability
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
cursor.execute(query)

# Weak hash algorithm
hashed = hashlib.md5(password.encode()).hexdigest()
print("MD5 Hash:", hashed)

# Command injection vulnerability
filename = input("Enter filename: ")
subprocess.call("cat " + filename, shell=True)

# Hardcoded password
admin_password = "admin123"

print("Login process completed")
