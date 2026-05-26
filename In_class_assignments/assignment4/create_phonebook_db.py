# problem 4
import sqlite3

def main():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()
    
    add_entries_table(cur)
    conn.commit()
    
    while True:
        print('\n--- Phonebook Menu ---')
        print('1. Add an entry')
        print('2. Look up a phone number')
        print('3. Update a phone number')
        print('4. Delete an entry')
        print('5. Display all entries')
        print('6. Exit')
        
        choice = input('Enter your choice (1-6): ')
        
        if choice == '1':
            add_entry(cur, conn)
        elif choice == '2':
            lookup_phone(cur)
        elif choice == '3':
            update_phone(cur, conn)
        elif choice == '4':
            delete_entry(cur, conn)
        elif choice == '5':
            display_entries(cur)
        elif choice == '6':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')
    
    conn.close()

def add_entries_table(cur):
    cur.execute('DROP TABLE IF EXISTS Entries')
    cur.execute('''CREATE TABLE Entries (EntryID INTEGER PRIMARY KEY AUTOINCREMENT,
                                         Name TEXT NOT NULL,
                                         Phone TEXT NOT NULL)''')

def add_entry(cur, conn):
    name = input('Enter name: ').strip()
    phone = input('Enter phone number: ').strip()
    
    if not name or not phone:
        print('Name and phone number cannot be empty.')
        return
    
    try:
        cur.execute('''INSERT INTO Entries (Name, Phone)
                       VALUES (?, ?)''', (name, phone))
        conn.commit()
        print(f'Entry for {name} added successfully.')
    except sqlite3.Error as e:
        print(f'Error adding entry: {e}')

def lookup_phone(cur):
    name = input('Enter name to look up: ').strip()
    
    if not name:
        print('Name cannot be empty.')
        return
    
    cur.execute('SELECT Name, Phone FROM Entries WHERE Name LIKE ?', (f'%{name}%',))
    results = cur.fetchall()
    
    if results:
        print(f'\nResults for "{name}":')
        for row in results:
            print(f'  {row[0]:20} {row[1]:20}')
    else:
        print(f'No entries found for "{name}".')

def update_phone(cur, conn):
    name = input('Enter name to update: ').strip()
    
    if not name:
        print('Name cannot be empty.')
        return
    
    cur.execute('SELECT EntryID, Name, Phone FROM Entries WHERE Name LIKE ?', (f'%{name}%',))
    results = cur.fetchall()
    
    if not results:
        print(f'No entries found for "{name}".')
        return
    
    if len(results) > 1:
        print('Multiple entries found:')
        for i, row in enumerate(results):
            print(f'  {i+1}. {row[1]} - {row[2]}')
        choice = input('Enter the number to update (or 0 to cancel): ')
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(results):
            print('Invalid choice.')
            return
        entry_id = results[int(choice)-1][0]
    else:
        entry_id = results[0][0]
    
    new_phone = input('Enter new phone number: ').strip()
    
    if not new_phone:
        print('Phone number cannot be empty.')
        return
    
    try:
        cur.execute('UPDATE Entries SET Phone = ? WHERE EntryID = ?', (new_phone, entry_id))
        conn.commit()
        print('Phone number updated successfully.')
    except sqlite3.Error as e:
        print(f'Error updating entry: {e}')

def delete_entry(cur, conn):
    name = input('Enter name to delete: ').strip()
    
    if not name:
        print('Name cannot be empty.')
        return
    
    cur.execute('SELECT EntryID, Name, Phone FROM Entries WHERE Name LIKE ?', (f'%{name}%',))
    results = cur.fetchall()
    
    if not results:
        print(f'No entries found for "{name}".')
        return
    
    if len(results) > 1:
        print('Multiple entries found:')
        for i, row in enumerate(results):
            print(f'  {i+1}. {row[1]} - {row[2]}')
        choice = input('Enter the number to delete (or 0 to cancel): ')
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(results):
            print('Invalid choice.')
            return
        entry_id = results[int(choice)-1][0]
    else:
        entry_id = results[0][0]
    
    confirm = input(f'Are you sure you want to delete this entry? (yes/no): ').lower()
    
    if confirm == 'yes':
        try:
            cur.execute('DELETE FROM Entries WHERE EntryID = ?', (entry_id,))
            conn.commit()
            print('Entry deleted successfully.')
        except sqlite3.Error as e:
            print(f'Error deleting entry: {e}')
    else:
        print('Deletion cancelled.')

def display_entries(cur):
    print('\n--- Phonebook Entries ---')
    cur.execute('SELECT * FROM Entries')
    results = cur.fetchall()
    
    if not results:
        print('No entries in phonebook.')
    else:
        print(f'{"ID":<5} {"Name":<20} {"Phone":<20}')
        print('-' * 45)
        for row in results:
            print(f'{row[0]:<5} {row[1]:<20} {row[2]:<20}')

if __name__ == '__main__':
    main()
