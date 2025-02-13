import _sqlite3
## connect to sqlite
connection=_sqlite3.connect("student.db")
## create a cursor object to insert record,create table,retrieve
cursor=connection.cursor()
##create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);

 """
cursor.execute(table_info)
 
## insert some more records
cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Vaidehi','Data Science','A',100)''')
cursor.execute('''Insert Into STUDENT values('Sanika','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Sandhya','Devops','A',50)''')
cursor.execute('''Insert Into STUDENT values('Samiksha','Devops','A',35)''')
## display all the records
print("The inserted records are")

data=cursor.execute('''Select * From STUDENT''')
for row in data:
    print(row)

## close the connection
connection.commit()
connection.close()

