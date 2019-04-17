class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print('Id: {}'.format(self.id))
        print('Name: {}'.format(self.name))


class Manager(Employee):
    def __init__(self, id, name, salary, rais):
        Employee.__init__(self, id, name)
        self.salary = salary
        self.rais = rais

    def display(self):
        Employee.display(self)
        print('Salary: {}'.format(self.salary))
        print('Designation: Manager')


class Developer(Employee):
    def __init__(self, id, name, salary, rais):
        Employee.__init__(self, id, name)
        self.salary = salary
        self.rais = rais

    def display(self):
        Employee.display(self)
        print('Salary: {}'.format(self.salary))
        print('Designation: Developer')


class Company:

    def __init__(self, name, employees):
        self.name =  name
        self.employees = employees

    def display(self):
        print("Company Name: {}".format(self.name))
        print('Employees info:')
        for employee in self.employees:
            employee.display()

    def add_employee(self, employee):
        self.employees.append(employee)

    def rais_salary(self, employee):
        employee.salary = employee.salary * employee.rais

    def rais_salary_for_all(self):
        for employee in self.employees:
            self.rais_salary(employee)

m1 = Manager(1,'Abcd',1000,1.3)
# m1.display()

d1 = Developer(2, 'Xyz', 700, 1.2)
# d1.display()

employees = [m1, d1]
c1 = Company('Codekul', employees)
c1.display()
c1.rais_salary_for_all()
c1.display()
