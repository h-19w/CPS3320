import employee
def main():
    

    for i in range(3):
        name = input('Enter employee name: ')
        department = input('Enter employee department: ')
        job_title = input('Enter employee job title: ')

        emp = employee.employee(name, department, job_title)

        print('Here is the data that you entered:')
        emp.get_name()
        emp.get_department()
        emp.get_job_title()


if __name__ == '__main__':
    main()

