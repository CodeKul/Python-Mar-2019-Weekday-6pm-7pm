class Employee:
    def __init__(self, name, empId):
        self.name = name
        self.empId = empId

    def display(self):
        print('Employee ID: {}\nName: {}'.format(self.empId, self.name))

    
class Manager(Employee):
    def __init__(self, name, empId, cabinId):
        self.cabinId = cabinId
        Employee.__init__(self, name, empId)

    def display(self):
        Employee.display(self)
        print('Cabin ID: {}'.format(self.cabinId))


class Developer(Employee):
    def __init__(self, name, empId, deskId):
        self.deskId = deskId
        Employee.__init__(self, name, empId)

    def display(self):
        Employee.display(self)
        print('Desk ID: {}'.format(self.deskId))


m1 = Manager('ABC', 1, 12)
m1.display()

d1 = Developer('XYZ', 2, 30)
d1.display()