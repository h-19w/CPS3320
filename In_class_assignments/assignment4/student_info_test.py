# problem 5
import sqlite3

def get_connection():
    conn = sqlite3.connect('students.db')
    conn.execute('PRAGMA foreign_keys = ON')
    return conn

def create_tables():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Majors (
                    MajorID INTEGER PRIMARY KEY,
                    MajorName TEXT NOT NULL
                )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS Departments (
                    DepartmentID INTEGER PRIMARY KEY,
                    DepartmentName TEXT NOT NULL
                )''')
    cur.execute('''CREATE TABLE IF NOT EXISTS Students (
                    StudentID INTEGER PRIMARY KEY,
                    StudentName TEXT NOT NULL,
                    MajorID INTEGER,
                    DepartmentID INTEGER,
                    FOREIGN KEY (MajorID) REFERENCES Majors(MajorID),
                    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
                )''')
    conn.commit()
    conn.close()

# majors menu

def majors_menu():
    while True:
        print('\n--- Majors Menu ---')
        print('1. Add a new major')
        print('2. Search for an existing major')
        print('3. Update an existing major')
        print('4. Delete an existing major')
        print('5. Show all majors')
        print('6. Exit to main menu')

        print('\n')
        choice = int(input('Enter the operation number: '))

        if choice == 6:
            break

        conn = get_connection()
        cur = conn.cursor()

        if choice == 1:
            name = input('Enter major name: ')
            cur.execute('INSERT INTO Majors (MajorName) VALUES (?)', (name,))
            print(f'Major "{name}" added.')

        elif choice == 2:
            name = input('Enter major name to search: ')
            cur.execute('SELECT * FROM Majors WHERE MajorName = ?', (name,))
            row = cur.fetchone()
            if row:
                print(f'Found: MajorID={row[0]}, MajorName={row[1]}')
            else:
                print(f'No major found with name "{name}".')

        elif choice == 3:
            name = input('Enter the major name to update: ')
            cur.execute('SELECT * FROM Majors WHERE MajorName = ?', (name,))
            row = cur.fetchone()
            if row:
                new_name = input('Enter new name: ')
                cur.execute('UPDATE Majors SET MajorName = ? WHERE MajorName = ?', (new_name, name))
                print(f'Major updated to "{new_name}".')
            else:
                print(f'No major found with name "{name}".')

        elif choice == 4:
            name = input('Enter major name to delete: ')
            cur.execute('SELECT * FROM Majors WHERE MajorName = ?', (name,))
            row = cur.fetchone()
            if row:
                cur.execute('DELETE FROM Majors WHERE MajorName = ?', (name,))
                print(f'Major "{name}" deleted.')
            else:
                print(f'No major found with name "{name}".')

        elif choice == 5:
            cur.execute('SELECT * FROM Majors ORDER BY MajorName ASC')
            rows = cur.fetchall()
            if rows:
                for row in rows:
                    print(f'MajorID={row[0]}, MajorName={row[1]}')
            else:
                print('No majors found.')

        conn.commit()
        conn.close()

# departments menu
def departments_menu():
    while True:
        print('\n--- Departments Menu ---')
        print('1. Add a new department')
        print('2. Search for an existing department')
        print('3. Update an existing department')
        print('4. Delete an existing department')
        print('5. Show all departments')
        print('6. Exit to main menu')

        print('\n')
        choice = int(input('Enter the operation number: '))

        if choice == 6:
            break

        conn = get_connection()
        cur = conn.cursor()

        if choice == 1:
            name = input('Enter department name: ')
            cur.execute('INSERT INTO Departments (DepartmentName) VALUES (?)', (name,))
            print(f'Department "{name}" added.')

        elif choice == 2:
            name = input('Enter department name to search: ')
            cur.execute('SELECT * FROM Departments WHERE DepartmentName = ?', (name,))
            row = cur.fetchone()
            if row:
                print(f'Found: DepartmentID={row[0]}, DepartmentName={row[1]}')
            else:
                print(f'No department found with name "{name}".')

        elif choice == 3:
            name = input('Enter department name to update: ')
            cur.execute('SELECT * FROM Departments WHERE DepartmentName = ?', (name,))
            row = cur.fetchone()
            if row:
                new_name = input('Enter new name: ')
                cur.execute('UPDATE Departments SET DepartmentName = ? WHERE DepartmentName = ?', 
                            (new_name, name))
                print(f'Department updated to "{new_name}".')
            else:
                print(f'No department found with name "{name}".')

        elif choice == 4:
            name = input('Enter department name to delete: ')
            cur.execute('SELECT * FROM Departments WHERE DepartmentName = ?', (name,))
            row = cur.fetchone()
            if row:
                cur.execute('DELETE FROM Departments WHERE DepartmentName = ?', (name,))
                print(f'Department "{name}" deleted.')
            else:
                print(f'No department found with name "{name}".')

        elif choice == 5:
            cur.execute('SELECT * FROM Departments ORDER BY DepartmentName ASC')
            rows = cur.fetchall()
            if rows:
                for row in rows:
                    print(f'DepartmentID={row[0]}, DepartmentName={row[1]}')
            else:
                print('No departments found.')

        conn.commit()
        conn.close()

# ─── STUDENTS ─────────────────────────────────────────────────────────────────

def students_menu():
    while True:
        print('\n--- Students Menu ---')
        print('1. Add a new student')
        print('2. Search for an existing student')
        print('3. Update an existing student')
        print('4. Delete an existing student')
        print('5. Show all students')
        print('6. Exit to main menu')

        print('\n')
        choice = int(input('Enter the operation number: '))

        if choice == 6:
            break

        conn = get_connection()
        cur = conn.cursor()

        if choice == 1:
            name = input('Enter student name: ')

            cur.execute('SELECT * FROM Majors ORDER BY MajorName ASC')
            majors = cur.fetchall()
            if not majors:
                print('No majors available. Please add a major first.')
                conn.close()
                continue
            print('Available majors:')
            for m in majors:
                print(f'  {m[0]}. {m[1]}')
            major_id = int(input('Enter MajorID: '))
            cur.execute('SELECT MajorID FROM Majors WHERE MajorID = ?', (major_id,))
            if not cur.fetchone():
                print('Invalid MajorID.')
                conn.close()
                continue

            cur.execute('SELECT * FROM Departments ORDER BY DepartmentName ASC')
            depts = cur.fetchall()
            if not depts:
                print('No departments available. Please add a department first.')
                conn.close()
                continue
            print('Available departments:')
            for d in depts:
                print(f'  {d[0]}. {d[1]}')
            dept_id = int(input('Enter DepartmentID: '))
            cur.execute('SELECT DepartmentID FROM Departments WHERE DepartmentID = ?', (dept_id,))
            if not cur.fetchone():
                print('Invalid DepartmentID.')
                conn.close()
                continue

            cur.execute('INSERT INTO Students (StudentName, MajorID, DepartmentID) VALUES (?, ?, ?)',
                        (name, major_id, dept_id))
            print(f'Student "{name}" added.')

        elif choice == 2:
            name = input('Enter student name to search: ')
            cur.execute('''SELECT s.StudentID, s.StudentName, m.MajorName, d.DepartmentName
                           FROM Students s
                           LEFT JOIN Majors m ON s.MajorID = m.MajorID
                           LEFT JOIN Departments d ON s.DepartmentID = d.DepartmentID
                           WHERE s.StudentName = ?''', (name,))
            row = cur.fetchone()
            if row:
                print(f'StudentID={row[0]}, Name={row[1]}, Major={row[2]}, Department={row[3]}')
            else:
                print(f'No student found with name "{name}".')

        elif choice == 3:
            name = input('Enter student name to update: ')
            cur.execute('SELECT * FROM Students WHERE StudentName = ?', (name,))
            row = cur.fetchone()
            if row:
                new_name = input(f'Enter new name (or press Enter to keep "{name}"): ')
                if not new_name:
                    new_name = name

                cur.execute('SELECT * FROM Majors ORDER BY MajorName ASC')
                majors = cur.fetchall()
                print('Available majors:')
                for m in majors:
                    print(f'  {m[0]}. {m[1]}')
                major_input = input(f'Enter new MajorID (or press Enter to keep {row[2]}): ')
                major_id = int(major_input) if major_input else row[2]

                cur.execute('SELECT * FROM Departments ORDER BY DepartmentName ASC')
                depts = cur.fetchall()
                print('Available departments:')
                for d in depts:
                    print(f'  {d[0]}. {d[1]}')
                dept_input = input(f'Enter new DepartmentID (or press Enter to keep {row[3]}): ')
                dept_id = int(dept_input) if dept_input else row[3]

                cur.execute('''UPDATE Students SET StudentName = ?, MajorID = ?, DepartmentID = ?
                               WHERE StudentName = ?''', (new_name, major_id, dept_id, name))
                print(f'Student "{name}" updated.')
            else:
                print(f'No student found with name "{name}".')

        elif choice == 4:
            name = input('Enter student name to delete: ')
            cur.execute('SELECT * FROM Students WHERE StudentName = ?', (name,))
            row = cur.fetchone()
            if row:
                cur.execute('DELETE FROM Students WHERE StudentName = ?', (name,))
                print(f'Student "{name}" deleted.')
            else:
                print(f'No student found with name "{name}".')

        elif choice == 5:
            cur.execute('''SELECT s.StudentID, s.StudentName, m.MajorName, d.DepartmentName
                           FROM Students s
                           LEFT JOIN Majors m ON s.MajorID = m.MajorID
                           LEFT JOIN Departments d ON s.DepartmentID = d.DepartmentID
                           ORDER BY s.StudentName ASC''')
            rows = cur.fetchall()
            if rows:
                for row in rows:
                    print(f'StudentID={row[0]}, Name={row[1]}, Major={row[2]}, Department={row[3]}')
            else:
                print('No students found.')

        conn.commit()
        conn.close()

# main 
def main():
    create_tables()

    while True:
        print('\n--- Main Menu ---')
        print('1. Majors')
        print('2. Departments')
        print('3. Students')
        print('4. Exit')

        print('\n')
        choice = int(input('Enter the table number: '))

        if choice == 4:
            print('Goodbye!')
            break
        elif choice == 1:
            majors_menu()
        elif choice == 2:
            departments_menu()
        elif choice == 3:
            students_menu()

if __name__ == '__main__':
    main()
