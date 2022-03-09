import sqlite3 as sql

connection=sql.connect("Hospital.db")

getPatientId=input("Enter the Patient ID Looking for : ")

result=connection.execute("select * from Patient where Patient_Id="+getPatientId+"")

for i in result:
    print(i)