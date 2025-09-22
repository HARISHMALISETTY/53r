import mysql.connector 
from db import info

try:
    conn=mysql.connector.connect(**info)
    print('connection successful')
except:
    print('not able to connect')
cursor=conn.cursor()


#to create database
query='CREATE DATABASE if not exists 10000CODERS_new'
cursor.execute(query)
#using/selecting database
cursor.execute('use 10000coders')

#creating a table with id,name,email,course,joined_date
try:
    create_table="""create table if not exists students_new_1(
    id INT AUTO_INCREMENT PRIMARY KEY,NAME VARCHAR(100),EMAIL VARCHAR(100),
    COURSE VARCHAR(100),JOINED_DATE DATE);"""
    cursor.execute(create_table)
    print('table created successfully')
except mysql.connector.errors.ProgrammingError as e :
    print(e)

#insert single row of data
def insertSingleRow(data):
    try:
        insertdata="""insert into students (name,email,course,joined_date) values(%s,%s,%s,%s)"""
        cursor.execute(insertdata,data)
        print('data inserted ')
    except:
        print('something went wrong')

# insertSingleRow(('suresh','suresh@gmail.com','PFS','2025-02-06'))
# insertSingleRow(('akhil','akhil@gmail,com','PFS','2025-06-06'))
# insertSingleRow((input('enter name:'),input('enter email:'),input('enter course'),input('enter joined date')))

# insert multiple rows at a time
# def insertMultipleRows(data):
#     try:
#         insertquery="""insert into students (name,email,course,joined_date) values (%s,%s,%s,%s)"""
#         cursor.executemany(insertquery,data)
#     except:
#         print('something went wrong')

# insertMultipleRows([('shanmukh','shanmukh@gmail.com','PFS','2025-05-06'),
#             ('tharun','tharun@gmail.com','PFS','2025-05-06'),
#             ('saranya','saranya@gmail.com','PFS','2025-05-06')])


# def getRecords():
#     try:
#         query='select * from students'
#         cursor.execute(query)
#         results=cursor.fetchall()
#         for row in results:
#             print(row)        
#     except:
#         print('error occurred')

# getRecords()

def getStudentsByCourse(course_name):
    try:
        query="""select * from students where course= %s"""
        print(query)
        cursor.execute(query,(course_name,))
        results=cursor.fetchall()
        for x in results:
            print(x)
        # print(results)
    except:
        print('something went wrong')

getStudentsByCourse('PFS')

#updaterecordwithnewemail
#deletesinglerecordbyemail
#deletemultiplerecordsbycourse




conn.commit()
cursor.close()
conn.close()
