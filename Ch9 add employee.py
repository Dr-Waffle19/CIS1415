
class Employee():
    def __init__(self, name, ID, Department, Job_Title):
        self.name = name
        self.ID = ID
        self.Department = Department 
        self.Job_Title = Job_Title

theCompany = [ ]

num_Employees = int(input('Enter number of employees: '))

for i in range(num_Employees):
    name = input('Enter name of employee: ')
    ID = input('Enter employee ID: ')
    Department  = input('Enter employee department: ')
    Job_Title = input('Enter job title: ')
    Employee_Data = Employee(name, ID, Department, Job_Title)
    theCompany.append(Employee_Data)

for i in range(num_Employees):
    print('{:<15}'.format(theCompany[i].name), '{:<10}'.format(theCompany[i].ID),
          '{:<10}'.format(theCompany[i].Department), '{:<15}'.format(theCompany[i].Job_Title))

