class Claculator:
    def __init__(self, opr1, opr2):
        self.op1 = opr1
        self.op2 = opr2
        self.res = 0

    def addition(self):
        self.res = self.op1 + self.op2
        self.display()

    def subtraction(self):
        self.res = self.op1 - self.op2
        self.display()

    def multiplication(self):
        self.res = self.op1 * self.op2
        self.display()

    def division(self):
        self.res = self.op1 / self.op2
        self.display()

    def display(self):
        print("Result: {}".format(self.res))
    

calc = Claculator(10, 20)
calc.addition()
calc.subtraction()
calc.multiplication()
calc.division()