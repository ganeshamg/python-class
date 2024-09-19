import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create the students table
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    address TEXT,
    blood_group TEXT,
    results TEXT
)
''')
conn.commit()

# Student data
students = [
    (1, 'Ram', '123 Main St, CityA', 'O+', 'Pass'),
    (2, 'Shyam', '456 Side St, CityB', 'A-', 'Pass'),
    (3, 'Hari', '789 Broad St, CityC', 'B+', 'Fail'),
    (4, 'Krishna', '321 High St, CityD', 'AB+', 'Pass'),
    (5, 'Govinda', '654 Low St, CityE', 'O-', 'Pass')
]

# Insert student data
cursor.executemany('''
INSERT INTO students (id, name, address, blood_group, results)
VALUES (?, ?, ?, ?, ?)
''', students)
conn.commit()

# Fetch and display the data
cursor.execute('SELECT * FROM students')
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the connection
conn.close()
