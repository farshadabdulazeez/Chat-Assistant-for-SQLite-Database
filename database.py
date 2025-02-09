import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('company.db')
cursor = conn.cursor()

# Create Employees table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Department TEXT,
    Salary INTEGER,
    Hire_Date TEXT
)
''')

# Create Departments table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Departments (
    ID INTEGER PRIMARY KEY,
    Name TEXT,
    Manager TEXT
)
''')

# Insert sample data into Employees table
employees_data = [
    (1, 'Alice', 'Sales', 50000, '2021-01-15'),
    (2, 'Bob', 'Engineering', 70000, '2020-06-10'),
    (3, 'Charlie', 'Marketing', 60000, '2022-03-20'),
    # Add more data here...
]

cursor.executemany('INSERT INTO Employees (ID, Name, Department, Salary, Hire_Date) VALUES (?, ?, ?, ?, ?)', employees_data)

# Insert sample data into Departments table
departments_data = [
    (1, 'Sales', 'Alice'),
    (2, 'Engineering', 'Bob'),
    (3, 'Marketing', 'Charlie'),
    # Add more data here...
]

cursor.executemany('INSERT INTO Departments (ID, Name, Manager) VALUES (?, ?, ?)', departments_data)

# Commit changes and close connection
conn.commit()
conn.close()