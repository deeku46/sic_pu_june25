import pymysql

def connect_db():
    connection = None
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="deeku46",
            database="deekshith_db",
            port=3306,
            charset="utf8"
        )
        print("Database connected")
    except:
        print("Database connection failed")
    return connection

def disconnect_db(connection):
    try:
        connection.close()
        print("Database disconnected")
    except:
        print("Database disconnection failed")

def creat_db():
    query = 'Create database IF NOT EXISTS deekshith_db'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print("Database created")
        cursor.close()
        disconnect_db(connection)
    except:
        print("Datbase creation failed")

def create_table():
    query = '''
    CREATE TABLE IF NOT EXISTS employee (
        ID INT PRIMARY KEY AUTO_INCREMENT,
        Emp_name VARCHAR(30),
        Designation VARCHAR(30),
        Phone_number BIGINT UNIQUE,
        Salary FLOAT,
        Commission FLOAT DEFAULT 0,
        Years_of_experience TINYINT,
        Technology VARCHAR(30) NOT NULL
    )
    '''
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print('Table created')
        cursor.close()
        disconnect_db(connection)
    except Exception as e:
        print('Table creation failed:', e)

def read_all_employees():
    query = 'select * from employee'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print('All rows retrived')
        
        cursor.close()
        disconnect_db(connection)
    except:
        print('Rows retrival failed')

def search_employees():
    query = 'select * from employee where id = %s'
    id = int(input("Enter Id of the employee to search: "))
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print('All rows retrived')
        
        cursor.close()
        disconnect_db(connection)
    except:
        print('Rows retrival failed')


creat_db()
create_table()
read_all_employees()
