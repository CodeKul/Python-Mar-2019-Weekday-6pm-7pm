# Assignment

a = 10
b = 20
res = 0

# Arithmetic
'''
    +
    -
    *
    /
    %
    **
'''

res = a + b
res = a - b
res = a * b
res = a / b
res = a % b
res = a ** 2 # square of a
res = a ** 3 # cube of a

# Compound assignment
'''
    +=
    -=
    *=
    /=
    %=
    **=
'''

res **= a # res = res + a


# Comparision
'''
    <
    >
    <=
    >=
    ==
    !=
'''

res = (a < b) + (a != 10)

# Logical 
'''
    and
    or
    not

    p   q   and or  not(p)
    t   t   t   t   f
    t   f   f   t   f
    f   t   f   t   t
    f   f   f   f   t
'''

res = not((a < b) or (b != 20))

print(res)