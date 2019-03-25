class Dog:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print('{} is eating'.format(self.name))

class Cat:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print('{} is eating'.format(self.name))


def feedAnimal(animal):
    animal.eat()


d = Dog('Tommy')
c = Cat('Dolly')

feedAnimal(d)
feedAnimal(c)