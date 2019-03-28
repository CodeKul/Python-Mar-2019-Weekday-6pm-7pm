'''
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
'''

# f = open("abc.txt", "a")
# f.write('\nThis is second line in file')
# f.close()

f = open("abc.txt", "rb")
# str = f.read(5)
# str = f.readline()
# print(str)
# str = f.readline()
# print(str)

# lines = f.readlines()
# print(lines)

f.seek(3, 0)
l1 = f.readline()
print(l1.decode('utf-8'))

f.seek(3, 1)
l2 = f.readline()
print(l2.decode('utf-8'))
