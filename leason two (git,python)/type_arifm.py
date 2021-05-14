
''' 13.05.2021 АРИФМЕТИЧЕСКИЕ ДЕЙСТВИЯ + ТИПЫ ДАННЫХ (МНОЖЕСТВА,СПИСКИ,СЛОВАРЬ)'''
#### АРИФМЕТИЧЕСКИЕ ДЕЙСТВИЯ
print('произведение')
a = 5 * 5
print('5 * 5 =', a, '\n')

print('частное')
a = 5 // 5
print('5 / 5 =', a, '\n')

print('разность')
a = 5 - 5
print('5 - 5 =', a, '\n')

print('сумма')
a = 5 + 5
print('5 + 5 =', a, '\n')

print('возведение в степень')
a = 2 ** 3
print('2 ** 3 = ', a, '\n')

print('остаток от деления')
a = 5 % 3
b = 5 % 5
print('5 % 3 = ', a)
print('5 % 5 = ', b)
print('\n\n')

#### ТИПЫ ДАННЫХ
print('ТИПЫ ДАННЫХ')
print('set,dict,list,string,integer,float,tuple', '\n')

### ИЗМЕНЯЕМЫЕ ТИПЫ
print('ИЗМЕНЯЕМЫЕ ТИПЫ')
print('set - множества')
print('dict - словарь')
print('list - список (лист или массив', '\n')

## МНОЖЕСТВА
print('МНОЖЕСТВА')
# СОЗДАНИЕ МНОЖЕСТВА
type_set = {1, '2', 3.0, 3.0}
print('тип множества (итерируемый,неиндексируемый, неупорядоченный, не имеет дубликатов)', type(type_set), type_set)
# ДОБАВЛЕНИЕ ЭЛЕМЕНТА В МНОЖЕСТВАХ КОМАНДОЙ .discard
type_set.add(4.0)
print('добавляем НЕ ИЗМЕНЯЕМЫЙ ОБЪЕКТ командой type_set.add(4.0): ', type_set)
# ПРИМЕР НЕ КОРРЕКТНОГО ДОБАВЛЕНИЯ ЭЛЕМЕНТА В МНОЖЕСТВАХ
try:
    type_set.add([4, 1, 2])
except Exception as ex:
    print('ошибка при добавлении ИЗМЕНЯЕМОГО ОБЪЕКТА командой type_set.add([4,1,2]):', ex)
# УДАЛЕНИЕ ЭЛЕМЕНТА ИЗ МНОЖЕСТВА КОМАНДОЙ .discard
type_set.discard(4.0)
print('удаляем НЕ ИЗМЕНЯЕМЫЙ ОБЪЕКТ командой type_set.discard(4.0): ', type_set)

## СПИСОК
print('СПИСОК')
# СОЗДАНИЕ ЛИСТА
type_list = [1, '2', 3.0, 3.0]
print('тип список (итерируемый,индексируемый, упорядоченный)', type(type_list), type_list)
# ДОБАВЛЕНИЕ ЭЛЕМЕНТА В СПИСОК КОМАНДОЙ .append
type_list.append(4.0)
print('добавляем НЕ ИЗМЕНЯЕМЫЙ ОБЪЕКТ командой type_list.append(4.0): ', type_list)
type_list.append([4, 1, 2])
print('добавляем ИЗМЕНЯЕМЫЙ ОБЪЕК командой type_list.append([4, 1, 2]): ', type_list)
# УДАЛЕНИЕ ПЕРВОГО НАЙДЕНОГО ЭЛЕМЕНТА В СПИСКЕ КОМАНДОЙ .remove
type_list.remove(3.0)
print('удаляем перввый найденый ОБЪЕКТ командой type_list.remove(3.0): ', type_list)

## СЛОВАРЬ
print('СЛОВАРЬ')
# СОЗДАНИЕ СЛОВАРЯ
type_dict = {1: 'one', 'two': 2, 3.0: 3}
print('тип словарь (итерируемый,индексируемый, неупорядоченные)', type(type_dict), type_dict)
# ДОБАВЛЕНИЕ КЛЮЧА И ЕГО ЗНАЧЕНИЯ В СПИСОК КОМАНДОЙ name_dict[KEY] = VALUE
type_dict[4.0] = 'four'
print("добавляем КЛЮЧ И ЕГО НЕ ИЗМЕНЯЕМОЕ ЗНАЧЕНИЕ командой type_dict[4.0] = 'four': ", type_dict)
type_dict['four, one, two'] = [4, 1, 2]
print("добавляем КЛЮЧ И ЕГО ИЗМЕНЯЕМЫЙ ЗНАЧЕНИЕ командой type_list[[4, 1, 2]] = ['four', 'one', 'two']: ", type_dict)
# УДАЛЕНИЕ КЛЮЧА И ЕГО ЗНАЧНИЯ ПО КЛЮЧУ КОМАНДОЙ .pop
type_dict.pop(4.0)
print('удаление ключа и его значения по ключу командой type_dict.pop(4.0) : ', type_dict)
print('\n')

### НЕ ИЗМЕНЯЕМЫЕ ТИПЫ
print('НЕИЗМЕНЯЕМЫЕ ТИПЫ')
print('bool - True/False')
print('int - целое число')
print('float - вещественное число')
print('tuple - кортеж')
print('str - строка', '\n')

# БУЛЕВ
type_bool = True
print('тип булев ', type(type_bool), type_bool)
# ЦЕЛОЕ ЧИСЛО
type_int = 150
print('тип интежер ', type(type_int), type_int)
# ВЕЩЕСТВЕННОЕ ЧИСЛО
type_float = 150.501
print('тип флоат ', type(type_float), type_float)
# КОРТЕЖ
type_tuple = ('one', 2, 3.0)
print('тип кортеж (итерируемый,неизменяемые, упорядоченные, без методов изменений) ', type(type_tuple), type_tuple)
# СТРОКА
type_str = ('one, 2, 3.0')
print('тип строка (итерируемый,упорядоченные символы) ', type(type_str), type_str)
print('\n')

### РАЗНИЦА ТИПОВ
print('РАЗНИЦА ТИПОВ')
print('мутабельные объекты - это изменяемые')
print('иммутабельные объекты - это неизменяемые')
a = ['one', 2, 3.0]
print('создаем список: ', a)
b = 'one, 2, 3.0'
print('создаем строку: ', b)
# СМОТРИМ АДРЕСА ОБЪЕКТОВ В ПАМЯТИ
print('адрес объекта a(список) :', id(a))
print('адрес объекта b(строка) :', id(b))
# ДОБАВЛЯЕМ НОВЫЙ ЭЛЕМЕНТ
a.append(4)
b = b + ', 4'
print('добавляем элемент к изменяемому объекту список, a.append(4) :', a)
print("добавляем элемент к неизменяемому объекту строка, b = b + ', 4' :", b)
# СМОТРИМ АДРЕСА ОБЪЕКТОВ В ПАМЯТИ ПОСЛЕ ВЗАИМОДЕЙСТВИЯ С НИМИ
print('адрес объекта a(список) после взаимодействия :', id(a))
print('адрес объекта b(строка) после взаимодействия :', id(b))
print('\n')


### КОНВЕРТАЦИЯ ТИПОВ
print('КОНВЕРТАЦИЯ ТИПОВ')
## INT --> FLOAT --> INT
print('INT --> FLOAT --> INT')
a = 1
print('тип объекта a = 1 :', a, type(a))
a = float(a)
print('тип объекта после конвертации во float, a = float(1) :', a, type(a))
a = int(a)
print('тип объекта после конвертации в int, a = int(a) :', a, type(a))

## INT --> STR --> FLOAT --> INT --> STR
print('INT --> STR --> FLOAT --> INT --> STR')
a = 1
print('тип объекта a = 1 :', a, type(a))
a = str(a)
print('тип объекта после конвертации в str, a = str(a) :', a, type(a))
a = float(a)
print('тип объекта после конвертации в float, a = float(a) :', a, type(a))
a = int(a)
print('тип объекта после конвертации во int, a = int(a) :', a, type(a))
a = str(a)
print('тип объекта после конвертации в str, a = str(a) :', a, type(a))

## LIST --> SET --> TUPLE --> LIST
print('LIST --> SET --> TUPLE --> LIST')
a = [1.0, 2, 'free']
print('тип объекта a = True :', a, type(a))
a = set(a)
print('тип объекта после конвертации в set, a = set(a) :', a, type(a))
a = tuple(a)
print('тип объекта после конвертации в tuple, a = tuple(a) :', a, type(a))
a = list(a)
print('тип объекта после конвертации в list, a = list(a) :', a, type(a))
print('\n\n')

#### УСЛОВНЫЕ КОНСТРУКЦИИ
print('УСЛОВНЫЕ КОНСТРУКЦИИ')
print('операторы <,>,==,!=')
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

# for i in type_set:
#     print('type_set =', i)
# print('\n\n')
# for i in type_list:
#     print('type_list =', i)
# print('\n\n')
# for i in type_dict:
#     print('type_dict =', i)
# print('\n\n')
####
type_dict = {1: 'one', 'two': 2, 3.0: 3}
type_list = [1, '2', 3.0, 3.0]
type_tuple = ('one', 2, 3.0,type_dict)
type_tuple_b = (type_list,type_tuple )
print(type_tuple_b)
print(type_tuple_b[0].pop())
print(type_tuple_b)
#type_set = {1, '2', 3.0, 3.0,type_dict}

