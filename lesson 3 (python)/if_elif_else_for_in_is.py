""" 18.05.2021 УСЛОВНЫЕ КОНСТРУКЦИИ И ЦИКЛЫ """
#### УСЛОВНЫЕ КОНСТРУКЦИИ
print('УСЛОВНЫЕ КОНСТРУКЦИИ')
print('операторы <,>,<=,>=,==,!=')
a = 1.0
b = 2.0

if a < b:
    print('"а" меньше(<) "b"')
elif a == b:
    print('"а" равно(==) "b"')

if a != b:
    print('"а" НЕравно(!=) "b"')
else:
    print('"a" больше "b"')
print('\n')

print("оператор is и in")
print('is - это сравнение адреса объекта в памяти')
print('in - это поиск значения в итерируемом объекте')
a = 1
b = 1
c = "1"
d = [1, 0, 2]

if a is b:
    print('"a" is "b"', id(a), id(b))

if a is int(c):
    print('"a" is "c"', id(a), id(c), type(int(c)), id(int(c)))

if a in d:
    print('"a" in "d"')

#### ЦИКЛЫ
print('ЦИКЛЫ')
print('циклы для списков, множества, кортежей, словарям')

type_list = [8, 9.0, 10, '11', [12, 13, '14']]
type_tuple = (8, 9.0, 10, '11', [12, 13, '14'])
type_set = {8, 9.0, 10, '11', (12, 13, '14')}
type_string = 'one'

## обычный цикл
print('обычный цикл листа')
for i in type_list:
    print('значение листа:', i)

print('\nобычный цикл кортежа')
for i in type_tuple:
    print('значение кортежа:', i)

print('\nобычный цикл множества')
for i in type_set:
    print('значение множества:', i)

print('\nобычный цикл строки')
for i in type_string:
    print('значение элемента строки:', i)
## цикл индексов
print('\nцикл кол-ва элементов листа')
print(len(type_list))
for i in range(len(type_list)):
    print('индекс листа:', i)

print('\nцикл кол-ва элементов кортежа')
for i in range(len(type_tuple)):
    print('индекс кортежа:', i)

print('\nцикл кол-ва элементов в множестве')
for i in range(len(type_set)):
    print('индекс множества:', i)

## цикл индексов и его значения
print('\nцикл индексов и его значения листа')
for i in range(len(type_list)):
    print('индекс:', i, 'значение индекса:', type_list[i])

print('\nцикл индексов и его значения кортежа')
for i in range(len(type_tuple)):
    print('индекс:', i, 'значение индекса:', type_tuple[i])

# ошибка, т.к мы знаем что множество итерируемый,неиндексируемый, неупорядоченный, не имеет дубликатов
print('\nцикл индексов и его значения множества')
for i in range(len(type_set)):
    print('индекс:', i, 'значение индекса:', type_set[i])


## вложенные циклы
print('\nцикл индексов и его значения листа')
type_list = [['восемь', '9.0', '10', '11'], ['12', '13', '14']]

print('\nзначение листа 1 уровня')
for i in type_list:
    print('значение листа 1 уровня:', i)

print('\nзначение листа 2 уровня')
for i in type_list:
    for j in i:
        print('значение листа 2 уровня:', j)

print('\nзначение листа 3 уровня')
for i in type_list:
    for j in i:
        for k in j:
            print('значение листа 3 уровня:', k)

## циклы словаря
type_dict = {1: "one", 2: 2.0, "last": [3, 4, 5]}
print('\nцикл словаря по ключам')
for key in type_dict:
    print('ключ словаря:', key)

print('\nцикл словаря по значениям')
for value in type_dict.values():
    print('значение словаря:', value)

print('\nцикл словаря по ключам и поиск значения по ключу')
for key in type_dict:
    print('ключ словаря:', key,'и его значение', type_dict[key])

print('\nцикл словаря по ключам и их значений')
for key, value in type_dict.items():
    print('ключ словаря:', key, 'и его значение', value)

## вложенные циклы и условные конструкции
type_list = [['восемь', '9.0', 'десять', '11'], ['12', '13', '14']]
print('\nвложенные циклы и условные конструкции 1 уровня')
for i in range(len(type_list)):
    if 'десять' in type_list[i]:
        print('значение "десять" содержиться в индексе:', i)

print('\nвложенные циклы и условные конструкции 2 уровня')
for i in range(len(type_list)):
    for j in range(len(type_list[i])):
        if 'десять' in type_list[i][j]:
            print('значение "десять" содержиться в индексе:', j)

print('\nвложенные циклы и условные конструкции 3 уровня')
for i in range(len(type_list)):
    for j in range(len(type_list[i])):
        for k in range(len(type_list[i][j])):
            if 'е' in type_list[i][j][k]:
                print('значение "е" содержиться в индексе:', k, 'слова: ', type_list[i][j])


