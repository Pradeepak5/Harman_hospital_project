import sqlite3

connection = sqlite3.connect("Hospital.db")
# connection.execute(''' CREATE TABLE IF NOT EXISTS DOCTORS(
#                 NAME TEXT,
#                 EMAIL_ID TEXT,
#                 QUALIFICATION TEXT,
#                 ADDRESS TEXT,
#                 PHNO TEXT
# );''')
#
# print("Table Creation Successful")

getName = input("Enter the Name : ")
getEmail = input("Enter the Email : ")
getQuali = input("Enter the Qualification : ")
getAdd = input("Enter Address : ")
getPhno = input("Enter Phone Number : ")

connection.execute("INSERT INTO DOCTORS(NAME,EMAIL_ID,QUALIFICATION,ADDRESS,PHNO) VALUES ('"+getName+"','"+getEmail+"','"+getQuali+"','"+getAdd+"','"+getPhno+"')")

print("Entry Created successfully")
connection.commit()
connection.close()
