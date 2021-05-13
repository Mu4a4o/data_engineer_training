
''' 11.05.2021 АРИФМЕТИЧЕСКИЕ ДЕЙСТВИЯ + ТИПЫ ДАННЫХ (МНОЖЕСТВА,СПИСКИ,СЛОВАРЬ)'''
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
print('____________________________________', '\n\n')

#### ТИПЫ ДАННЫХ
print('ТИПЫ ДАННЫХ')
print('set,dict,list,string,integer,float,tuple', '\n')

### ИЗМЕНЯЕМЫЕ ТИПЫ
print('ИЗМЕНЯЕМЫЕ ТИПЫ')
print('set = множества')
print('dict = словарь')
print('list = список (лист или массив', '\n')

## МНОЖЕСТВА
print('МНОЖЕСТВА')
# СОЗДАНИЕ МНОЖЕСТВА
type_set = {1, '2', 3.0, 3.0}
print('тип множества (не индексируемый, неупорядоченный, не имеет дубликатов)', type(type_set), type_set)
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
print('тип список (индексируемый, упорядоченный)', type(type_list), type_list)
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
print('тип словарь (индексируемый, неупорядоченные)', type(type_dict), type_dict)
# ДОБАВЛЕНИЕ КЛЮЧА И ЕГО ЗНАЧЕНИЯ В СПИСОК КОМАНДОЙ name_dict[KEY] = VALUE
type_dict[4.0] = 'four'
print("добавляем КЛЮЧ И ЕГО НЕ ИЗМЕНЯЕМОЕ ЗНАЧЕНИЕ командой type_dict[4.0] = 'four': ", type_dict)
type_dict['four, one, two'] = [4, 1, 2]
print("добавляем КЛЮЧ И ЕГО ИЗМЕНЯЕМЫЙ ЗНАЧЕНИЕ командой type_list[[4, 1, 2]] = ['four', 'one', 'two']: ", type_dict)
# УДАЛЕНИЕ КЛЮЧА И ЕГО ЗНАЧНИЯ ПО КЛЮЧУ КОМАНДОЙ .pop
type_dict.pop(4.0)
print('удаление ключа и его значения по ключу командой type_dict.pop(4.0) : ', type_dict)


# for i in type_set:
#     print('type_set =', i)
# print('\n\n')
# for i in type_list:
#     print('type_list =', i)
# print('\n\n')
# for i in type_dict:
#     print('type_dict =', i)
# print('\n\n')
