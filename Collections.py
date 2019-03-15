# 1) String

str1 = "Codekul"
str2 = 'The Gurukul for Coders!'

# 'Codekul' - "The Gurukul for Coders!"

str3 = """'{}'
    "{}"
        Python""".format(str1, str2)

'''
\n
\b
\t
\r
'''

str4 = 'Codekul - \rThe Gurukul for Coders!'

str5 = str4.replace(' ','_',-1)

# print(str5)

# 2) List

list1 = [1,2,3,4,5,"Six", "Seven", 9.10, True]
list2 = ["A", "B", "C"]

list3 = list1 + list2

c = list3.count("A")

length = len(list3)

# print(length)

# 3) Dictionary

dict1 = {"Key1": "Value1", "Key2": "Value2", "Key3": 3}

# print(dict1["Key1"])

# 4) Tuple

t1 = (1,2,3,4,5)

# print(t1)


# for loop

for (index, data) in enumerate(list1):
    print("Index: {} - {}".format(index, data))