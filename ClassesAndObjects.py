class MyClass:

    name = ''

    def display(self):
        print("This is my class")
        print('My name is {}'.format(self.name))



myObj = MyClass()

myObj.display()

myObj.name = 'Codekul'

myObj.display()