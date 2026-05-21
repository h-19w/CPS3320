import sqlite3

def main():
    # Connect to the database.
    conn = sqlite3.connect('inventory.db')
    
    # Get a cursor.
    cur = conn.cursor()

    # cur.execute('''SELECT * FROM Inventory WHERE Price > 10''')
    # cur.execute('''SELECT MAX(Price) FROM Inventory WHERE Price > 10''')
    # cur.execute('''SELECT MIN(price) FROM Inventory WHERE Price > 10''')
    # cur.execute('''SELECT SUM(Price) FROM Inventory WHERE Price > 10''')
    cur.execute('''SELECT COUNT(*) FROM Inventory WHERE Price > 3''')
    rows = cur.fetchone()
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