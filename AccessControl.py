class MyClass:

    def __init__(self):
        self.a = 10
        self.__b = 20

    def display(self):
        print('a: {}\nb: {}'.format(self.a, self.__b))

    def __set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.__b = b

    def input(self, a, b):
        self.__set_a(a)
        self.set_b(b)


my_Obj = MyClass()

my_Obj.display()

my_Obj.a = 100
my_Obj.__b = 200

my_Obj.display()

# my_Obj.__set_a(1000)
# my_Obj.set_b(2000)

my_Obj.input(1000, 2000)

my_Obj.display()
