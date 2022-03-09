import sqlite3 as sql

connection=sql.connect("Hospital.db")

getPatientId=input("Enter id which want to delete : ")

connection.execute("delete from Patient where Patient_Id="+getPatientId+"")

print("data deleted successfully")

result=connection.execute("select * from Patient")

for i in result:
    print(i)