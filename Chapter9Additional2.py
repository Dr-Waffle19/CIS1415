#Initializes the class Employee with a constructor (__init__) and one method.
class Employee:

    #Basic constructor with four attributes: name, id_num, depart, and title
    def __init__(self, name='none', id_num=0, depart='none', title='none'):
        self.name = name
        self.id_num = id_num
        self.depart = depart
        self.title = title

    #Method formats and prints out employee data in a table-like fashion
    def print_employee(self):
        return ('%-20s %-20d %-20s %-20s' % (self.name, self.id_num,
                                             self.depart, self.title))

if __name__ == '__main__':

    #Block of code takes user entered data and stores it under seperate
    #variables to be used later in the calling of the Employee class.
    name1 = str(input('Enter employee 1\'s Name:\n').strip())
    id_num1 = int(input('Enter employee 1\'s ID Number:\n').strip())
    depart1 = str(input('Enter employee 1\'s Department:\n').strip())
    title1 = str(input('Enter emplyee 1\'s Job Title:\n').strip())

    #Calling of the Employee class using previously stored entered data.
    employee1 = Employee(name1, id_num1, depart1, title1)

    #Block of code takes user entered data and stores it under seperate
    #variables to be used later in the calling of the Employee class.
    name2 = str(input('\nEnter employee 2\'s Name:\n').strip())
    id_num2 = int(input('Enter employee 2\'s ID Number:\n').strip())
    depart2 = str(input('Enter employee 2\'s Department:\n').strip())
    title2 = str(input('Enter emplyee 2\'s Job Title:\n').strip())

    #Calling of the Employee class using previously stored entered data.
    employee2 = Employee(name2, id_num2, depart2, title2)

    #Block of code takes user entered data and stores it under seperate
    #variables to be used later in the calling of the Employee class.
    name3 = str(input('\nEnter employee 3\'s Name:\n').strip())
    id_num3 = int(input('Enter employee 3\'s ID Number:\n').strip())
    depart3 = str(input('Enter employee 3\'s Department:\n').strip())
    title3 = str(input('Enter emplyee 3\'s Job Title:\n').strip())

    #Calling of the Employee class using previously stored entered data.
    employee3 = Employee(name3, id_num3, depart3, title3)

    #Block of code used for formatting of priting out chart used later in file.
    p_name = 'Name'
    p_id_num = 'ID Number'
    p_depart = 'Department'
    p_title = 'Job Title'

    #First prints out the headers of the chart, and then calls the Employee
    #class method (print_employee) for each employee entered and prints it out.
    print('\n%-20s %-20s %-20s %-20s' % (p_name, p_id_num, p_depart, p_title))
    print(employee1.print_employee())
    print(employee2.print_employee())
    print(employee3.print_employee())
    
