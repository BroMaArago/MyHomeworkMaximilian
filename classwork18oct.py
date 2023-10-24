sample_tuple = (0, "dog", {0: "dog"})

sample_dict = {0: "dog", 1: "cat"}
print(type(sample_dict))

sample_dict[0]
sample_dict[1]

sample_dict = dict()
sample_dict[0] = "dog"
sample_dict[1] = "cat"

sample_dict = {0: "dog"}
# перезаписывание
sample_dict[0] = "cat"
# создание новой записи
sample_dict[1] = "cat"

list = [1, 2, 3, 4, 5]
for element in list:
    print(element)

a = "strings"
for elem in a:
    print(elem)

a = {"Key": 90, "Key0": 90}

for key, value in a.items():
    print(key, value)

# Множества
a = {0, 0, 0, 1}
print(a)

# множества есть изменяемы и неизменяемые
a.add(8)
print(a)

a = []
for i in range(1, 10):
    a.append(i)
b = [i for i in range(1, 10)]
print(a)
print(b)

a = []
for i in sample_string:
    if i in vowels:
        a.append(i)

b = [i for i in sample_string if i in vowels]
print(a)
print(b)

matrix = [[1, 10], [2, 20], [3, 30]]
one_dim = [j for i in matrix for j in i]
print(one_dim)
#1
a = [i for i in range (4,24,2)]
print(a)
#2
a = [i ** 2 for i in range (1,6)]
print(a)
#3
a = [i for i in range(11)]
print(a)
a = [i for i in range(1,11)]
print(a)
nums = [i for i in range(11) if i % 2 != 0]
print(nums)
nums = [i for i in a if i % 2 != 0]
print(nums)
#4
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
sample_tuple = (0, "dog", {0: "dog"})

sample_dict = {0: "dog", 1: "cat"}
print(type(sample_dict))

sample_dict[0]
sample_dict[1]

sample_dict = dict()
sample_dict[0] = "dog"
sample_dict[1] = "cat"

sample_dict = {0: "dog"}
# перезаписывание
sample_dict[0] = "cat"
# создание новой записи
sample_dict[1] = "cat"

list = [1, 2, 3, 4, 5]
for element in list:
    print(element)

a = "strings"
for elem in a:
    print(elem)

a = {"Key": 90, "Key0": 90}

for key, value in a.items():
    print(key, value)

# Множества
a = {0, 0, 0, 1}
print(a)

# множества есть изменяемы и неизменяемые
a.add(8)
print(a)

a = []
for i in range(1, 10):
    a.append(i)
b = [i for i in range(1, 10)]
print(a)
print(b)

a = []
for i in sample_string:
    if i in vowels:
        a.append(i)

b = [i for i in sample_string if i in vowels]
print(a)
print(b)

matrix = [[1, 10], [2, 20], [3, 30]]
one_dim = [j for i in matrix for j in i]
print(one_dim)
#1
a = [i for i in range (4,24,2)]
print(a)
#2
a = [i ** 2 for i in range (1,6)]
print(a)
#3
a = [i for i in range(11)]
print(a)
a = [i for i in range(1,11)]
print(a)
nums = [i for i in range(11) if i % 2 != 0]
print(nums)
nums = [i for i in a if i % 2 != 0]
print(nums)
#4
a = ["Words", "are", "difFerent"]
names_lower = [a.lower() for i in names]
print(names_lower)


#1 Сделать одномерным список [[1,2,3], [4,5]]
nested_list = [[1, 2, 3], [4,5]]
flat_list = [j for i in nested_list for j in i]
print(flat_list)



for i in nested_list:
    for j in i:
        print(j)

[j for i in nested_list for j in i]



matrix = [[90, 8], [1], [12, 45]]
print(matrix)

for i in matrix
    print(i)

matrix = [[90, 8], [1], [12, 45]]
print(matrix)

for i in matrix:
    print(i)

for i in matrix:
    for j in i:
print(j)

#2
[(n, n**2) range for n in range(1, 6)]

#3
sentence ='This is a sample sentenceee'
[i for i in sentence.split() if len(i) > 4]

words = sentence.split()
words
a = []
for word in words:
    if len(words) > 4:
        a.append(word)
print(a)
l = []
for n in range(1, 6):
    temp = (n, n**2)
    l.append(temp)
print(l)