import sqlite3

def create_student_info_db():
    """Create student_info.db with Majors, Department, and Students tables."""
    
    # Connect to the database (creates it if it doesn't exist)
    conn = sqlite3.connect('student_info.db')
    cursor = conn.cursor()
    
    # Create Majors table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Majors (
            MajorID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL
        )
    ''')
    
    # Create Department table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Department (
            DeptID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL
        )
    ''')
    
    # Create Students table with foreign keys
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Students (
            StudentID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            MajorID INTEGER,
            DeptID INTEGER,
            FOREIGN KEY (MajorID) REFERENCES Majors(MajorID),
            FOREIGN KEY (DeptID) REFERENCES Department(DeptID)
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database 'student_info.db' created successfully!")

if __name__ == '__main__':
    create_student_info_db()
