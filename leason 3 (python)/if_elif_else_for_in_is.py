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
elif a != b:
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
d = [1, 0]

if a is b:
    print('"a" is "b"', id(a), id(b))
if a is c:
    print('"a" is "c"')
if a in d:
    print('"a" in "d"')

#### ЦИКЛЫ
print('ЦИКЛЫ')
print('циклы для списков, множества, кортежей')

type_list = [8, 9.0, 10, '11', [12, 13, '14']]
type_tuple = (8, 9.0, 10, '11', [12, 13, '14'])
type_set = {8, 9.0, 10, '11', (12, 13, '14')}

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

## цикл индексов
print('\nцикл индексов листа')
for i in range(len(type_list)):
    print('индекс листа:', i)

print('\nцикл индексов кортежа')
for i in range(len(type_tuple)):
    print('индекс кортежа:', i)

print('\nцикл индексов множества')
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

## цикл индексов и его значения
print('\nцикл индексов и его значения листа')
for i in range(len(type_list)):
    print('индекс листа:', i, 'значение индекса листа:', type_list[i])

print('\nцикл индексов и его значения кортежа')
for i in range(len(type_tuple)):
    print('индекс кортежа:', i, 'значение индекса кортежа:', type_tuple[i])

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
