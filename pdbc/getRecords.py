# import mysql.connector 
# from db import info

# try:
#     conn=mysql.connector.connect(**info)
#     print('connection successful')
# except:
#     print('not able to connect')
# cursor=conn.cursor()

def getRecords():
    try:
        cursor.execute('use 10000coders')
        query='select * from students'
        cursor.execute(query)
        results=cursor.fetchall()
        for row in results:
            print(row)        
    except:
        print('error occurred')
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
def getLimitedRecords(limit):
    try:
        query="""select * from students  order by name asc limit %s"""
        cursor.execute(query,(limit,))
        result=cursor.fetchall()
        print(result)
    except:
        print("something went wrong")
    finally:
        print("task completed")