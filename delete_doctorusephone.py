import sqlite3
conn = sqlite3.connect("Hospital.db")
getPhno = input("Enter the Phone Number= ")
conn.execute("DELETE FROM DOCTORS WHERE PHNO='"+getPhno+"'")
conn.commit()
print("Entry Deleted successfully")
result = conn.execute("SELECT * FROM DOCTORS")
print("UPDATED RECORD")
for i in result:
    print("Name-", i[0])
    print("Email-", i[1])
    print("Qualification-", i[2])
    print("Address-", i[3])
    print("Phone Number-", i[4])
