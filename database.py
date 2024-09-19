import mysql.connector

# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
# )
# print(db)
# try:
    
#     cursor = db.cursor()
#     cursor.execute("create database pythonAUG")
# except:
#     print("database already exists")


db = mysql.connector.connect(
    host="localhost",
    user="root",
    database ="amgain"
)
print(db)
cursor = db.cursor()
# cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(30))")
# cursor.execute("INSERT INTO `customers` (`name`, `address`) VALUES ('Manoj Adhikari', 'Kalanki')")

# db.commit()

# command = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#     ('sudan', 'dang'),
#     ('suman', 'pokhara'),
#     ('aditya', 'kathmandu')
# ]
# cursor.executemany(command,val)
db.commit()

# Fetch data from database
'''
command = "Select * from customers"
cursor.execute(command)
a = cursor.fetchall()
for i in a:
    print(i)
'''

command = "Update customers set address = 'nepalgunj' where name = suman"
cursor.execute(command)
db.commit()

# delete
