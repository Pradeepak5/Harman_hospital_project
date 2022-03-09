import sqlite3
conn = sqlite3.connect("Hospital.db")
result = conn.execute("SELECT * FROM DOCTORS")
for i in result:
    print(i)