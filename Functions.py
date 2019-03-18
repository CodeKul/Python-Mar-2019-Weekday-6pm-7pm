# Function defination
def my_function():
    print('This is my_function')

# Function call
my_function()

def function_with(param1, param2, param3):
    print("Value of param1: {}".format(param1))
    print("Value of param2: {}".format(param2))
    print("Value of param3: {}".format(param3))

my_int = 200
function_with("Codekul", my_int, True)

def function_with_default_parameter(param1, param2=10):
    print("Value of param1: {}".format(param1))
    print("Value of param2: {}".format(param2))

function_with_default_parameter(20)

def function_with_returning():
    return 'Codekul'

str = function_with_returning()
print(str)

def add(num1, num2):
    res = num1 + num2
    return res

a = 10
b = 20
print(add(a, b))