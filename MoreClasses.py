class Triangle:
    def __init__(self, height, base):
        self.height = height
        self.base = base
        print('__init__')

    def display(self):
        print('Height: {}'.format(self.height))
        print('Base: {}'.format(self.base))

    # def display(self, name):
    #     self.display()
    #     print('Name: {}'.format(name))

    def area(self):
        a = 0.5 * self.base * self.height
        return a


t1 = Triangle(10, 20)
t1.display()
print('Area: {}'.format(t1.area()))