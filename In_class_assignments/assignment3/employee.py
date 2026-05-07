class employee:
    def __init__(self, name, department, job_title):
        self.__name = name
        self.__department = department
        self.__job_title = job_title

    def set_name(self, name):
        self.__name = name
    def set_department(self, department):
        self.__department = department
    def set_job_title(self, job_title):
        self.__job_title = job_title
    def get_name(self):
        print("Name: ", self.__name)
        return self.__name
    def get_department(self):
        print("Department: ", self.__department)    
        return self.__department
    def get_job_title(self):
        print("Job Title: ", self.__job_title)
        return self.__job_title
    