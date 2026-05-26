# problem 5 
import sqlite3

def main():
    conn = sqlite3.connect('students.db')
    cur = conn.cursor()

    add_majors_table(cur)
    add_departments_table(cur)
    add_students_table(cur)

    add_students(cur)

    display_majors(cur)
    display_departments(cur)
    display_students(cur)

    conn.commit()
    conn.close()

def add_majors_table(cur):
    cur.execute('DROP TABLE IF EXISTS Majors')
    cur.execute('''CREATE TABLE Majors (MajorID INTEGER PRIMARY KEY NOT NULL,
                                       MajorName TEXT)''')
    majors = [(1, 'Computer Science'),
              (2, 'Mathematics'),
              (3, 'Physics'),
              (4, 'Chemistry'),
              (5, 'Biology')]
    for major in majors:
        cur.execute('''INSERT INTO Majors (MajorID, MajorName)
                       VALUES (?, ?)''', major)

def add_departments_table(cur):
    cur.execute('DROP TABLE IF EXISTS Departments')
    cur.execute('''CREATE TABLE Departments (DepartmentID INTEGER PRIMARY KEY NOT NULL,
                                            DepartmentName TEXT)''')
    departments = [(1, 'Engineering'),
                   (2, 'Science'),
                   (3, 'Arts')]
    for dept in departments:
        cur.execute('''INSERT INTO Departments (DepartmentID, DepartmentName)
                       VALUES (?, ?)''', dept)

def add_students_table(cur):
    cur.execute('DROP TABLE IF EXISTS Students')
    cur.execute('''CREATE TABLE Students (StudentID INTEGER PRIMARY KEY NOT NULL,
                                         StudentName TEXT,
                                         MajorID INTEGER,
                                         DepartmentID INTEGER,
                                         FOREIGN KEY (MajorID) REFERENCES Majors(MajorID),
                                         FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID))''')

def add_students(cur):
    students = [(1, 'Alice', 1, 1),
                (2, 'Bob', 2, 2),
                (3, 'Charlie', 3, 2),
                (4, 'David', 4, 2),
                (5, 'Eve', 5, 3)]
    for student in students:
        cur.execute('''INSERT INTO Students (StudentID, StudentName, MajorID, DepartmentID)
                       VALUES (?, ?, ?, ?)''', student)

def display_majors(cur):
    cur.execute('SELECT * FROM Majors')
    rows = cur.fetchall()
    for row in rows:
        print(f'MajorID: {row[0]}, MajorName: {row[1]}')

def display_departments(cur):
    cur.execute('SELECT * FROM Departments')
    rows = cur.fetchall()
    for row in rows:
        print(f'DepartmentID: {row[0]}, DepartmentName: {row[1]}')

def display_students(cur):
    cur.execute('''SELECT s.StudentName, m.MajorName, d.DepartmentName
                   FROM Students s
                   JOIN Majors m ON s.MajorID = m.MajorID
                   JOIN Departments d ON s.DepartmentID = d.DepartmentID''')
    rows = cur.fetchall()
    for row in rows:
        print(f'Student: {row[0]}, Major: {row[1]}, Department: {row[2]}')

if __name__ == '__main__':
    main()

