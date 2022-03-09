import sqlite3 as sql

connection=sql.connect("Hospital.db")

getPatientId=input("Enter the Patient Id which want to update : ")

getNewPatientName=input("Enter the new name :")
getNewAddress=input("Enter the Address :")
getNewPhonenum=input("enter the phone number :")
getNewMail=input("Enter Mail Id :")
getNewPincode=input("Enter Pincode :")

result=connection.execute("update Patient set Patient_name="+getNewPatientName+", Patient_address='"+getNewAddress+"',Patient_phonenum="+getNewPhonenum+",Patient_email='"+getNewMail+"',Patient_pincode="+getNewPincode+" where Patient_Id="+getPatientId+"")

connection.commit()

print("updated successfully")

result=connection.execute("select * from Patient where Patient_Id="+getPatientId)

for i in result:
    print(i)