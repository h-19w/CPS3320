# problem 3
import sqlite3
def main():
    conn = sqlite3.connect('cities.db')

    cur = conn.cursor()
    
    print('1. Display cities by population (ascending)')
    print('2. Display cities by population (descending)')
    print('3. Display cities by name (ascending)')
    print('4. Display the total population')
    print('5. Display the average population')
    print('6. Display the maximum population')
    print('7. Display the minimum population')
    print('8. Display the number of cities')

    print ('\n')
    choice = int(input('Enter the operation number: '))
    
    if choice == 1:
        cur.execute('''SELECT *
                        FROM cities
                        ORDER BY population ASC;
                        ''')
    elif choice == 2:
        cur.execute('''SELECT *
                        FROM cities
                        ORDER BY population DESC;
                        ''')
    elif choice == 3:  
        cur.execute('''SELECT *
                        FROM cities
                        ORDER BY city_name ASC;
                        ''')
    elif choice == 4:
        cur.execute('''SELECT SUM(population) 
                    FROM cities;''')
    elif choice == 5:
        cur.execute('''SELECT AVG(population)
                        FROM cities;''')
    elif choice == 6:
        cur.execute('''SELECT MAX(population) FROM cities''')
    elif choice == 7:
        cur.execute('''SELECT MIN(population) FROM cities''')
    elif choice == 8:
        cur.execute('''SELECT COUNT(*) FROM cities''')
    
    rows = cur.fetchone()
    while rows is not None:
        print(rows)
        rows = cur.fetchone()

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
    