#for executing connection with database
import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user='root',
    password='',
    database='fayasdb'
)
mycursor=mydb.cursor()
#for creation of table
tablename=input("Enter table name")
columname1=input("Enter the first column name")
columname2=input("Enter the second column name")
columname3=input("Enter the third column name")
mycursor.execute('Create Table {}({} int,{} varchar(55),{} varchar(55))'.format(tablename,columname1,columname2,columname3))
#for inserting and updation of the values
def updates():
    data=int(input("Enter the data length"))
    for i in range(data):
        value1=input("Enter your {}".format(columname1))
        value2=input("Enter your {}".format(columname2))
        value3=input("Enter your {}".format(columname3))
        query1=("INSERT INTO {}({},{}) VALUES (%s,%s)".format(tablename,columname1,columname2))
        mycursor.executemany(query1,[(value1,value2,value3)])
        mydb.commit()
#for deleting data from table
def delete():
    delete_column=input("Enter the name you want to delete")
    delete_values="delete from {} where {}='{}'".format(tablename,columname2,delete_column)
    #columname2 is given based on my condition you can give any column name based on your preference
    mycursor.execute(delete_values)
    mydb.commit()
#for reading and printing the data
def read():
    sql="select * from {}".format(tablename)
    mycursor.execute(sql)
    result=mycursor.fetchall()
    for x in result:
        print(x)
#for repetedily asking the users choice
while True:
    userchoice=input("Enter your choice you want to update or delete or read")
    if userchoice.lower()[0]=='u':
        updates()
    elif userchoice.lower()[0]=='d':
        delete()
    elif userchoice.lower()[0]=='r':
        read()
    elif userchoice.lower()[0]=='e':
        break
    else:
        print("please enter a valid choice")
