a = 10
b = 5

'''
if condition:
    statements
'''

'''
if a < b:
    print('a is less than b')
    print('This is inside if')
print('This is outside if')
'''

if a < b:
    print('a is less than b')
    if a == 10:
        print('a is equal to 10')
    else:
        print('a is not equal to 10')
elif a == b:
    print('a and b are equal')
else:
    print('a is greater than b')

# Loops

'''
initialisation
while condition:
    statements
    incr/decr
'''

i = 0
while i < 10:
    if i % 2 == 0:
        print('Codekul')
    else:
        print('The Gurukul for Coders!')
    i += 1
