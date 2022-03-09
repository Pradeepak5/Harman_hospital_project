import sqlite3 as sql

connection=sql.connect("Hospital.db")

result=connection.execute("select * from Patient")

for i in result:
    print("Patient Id :",i[0])
    print("Patient Name :",i[1])
    print("Patient Address :",i[2])
    print("Patient Phone number :",i[3])
    print("Patient mailId :",i[4])
    print("Patient Pincode :",i[5])


