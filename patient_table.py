import sqlite3 as sql

connection=sql.connect("Hospital.db")

# connection.execute(''' create table Patient(
#                             Patient_Id integer,
#                             Patient_name text,
#                             Patient_address text,
#                             Patient_phonenum integer,
#                             Patient_email text,
#                             Patient_pincode integer
#                             );''')

print("patient table created successfully.")

getPatientId=input("Enter Patient Id :")
getPatientName=input("Enter the name :")
getAddress=input("Enter patient address :")
getPhoneNum=input("Enter mobile number :")
getmail=input("Enter the mail id :")
getPincode=input("Enter the pincode :")

connection.execute("insert into Patient(Patient_Id,Patient_name,Patient_address,Patient_phonenum,Patient_email,Patient_pincode)\
                   values("+getPatientId+",'"+getPatientName+"','"+getAddress+"',"+getPhoneNum+",'"+getmail+"',"+getPincode+")")

connection.commit()
connection.close()

print("Numbers inserted successfully.")

