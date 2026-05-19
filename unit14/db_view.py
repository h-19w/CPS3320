import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('inventory.db')
    
    # Get a cursor.
    cur = conn.cursor()

    cur.execute('''SELECT * FROM Inventory''')
    rows = cur.fetchone()
    print(rows, '\n')
    while rows is not None:
        print(rows)
        rows = cur.fetchone()   
        # fetchone() returns None when there are no more rows to fetch, so we can use that as a loop-control variable
    
    # Commit the changes.
    conn.commit()
    
    # Close the connection.
    conn.close()


if __name__ == '__main__':
    main()