""" 20.05.2021 УСЛОВНЫЕ КОНСТРУКЦИИ И ЦИКЛЫ (ПРИМЕРЫ С ИЗМЕНЕНИЕМ)  """
#### УСЛОВНЫЕ КОНСТРУКЦИИ И ЦИКЛЫ (ПРИМЕРЫ С ИЗМЕНЕНИЕМ)
import random


print('УСЛОВНЫЕ КОНСТРУКЦИИ И ЦИКЛЫ (ПРИМЕРЫ С ИЗМЕНЕНИЕМ) И СПЕЦИАЛЬНЫЕ ФУНКЦИИ(lambda,zip,map')

print('\nгенератор случайных чисел :', random.randrange(0, 50))

# создаем лист запоненый случаными значениями
type_list_random = [random.randrange(0, 50) for i in range(0, 50)]
# простой вариант верхней логики описан ниже
type_list_random_primer = []
for i in range(0, 50):
    type_list_random_primer.append(random.randrange(0, 50))
print(type_list_random_primer)
print('сгенерировали случайный список :', type_list_random)

# создаем словарь запоненый случаными ключами где True или False это их значения
type_dict_random = {random.randrange(0, 10): random.choice([True, False]) for i in range(0, 10)}
# простой вариант верхней логики описан ниже
type_dict_random_primer = {}
for i in range(0, 5):
    key = random.randrange(0,3)
    value = random.choice([True, False])
    print(key, value)
    type_dict_random_primer[2] = True
    type_dict_random_primer[key] = value
print(type_dict_random_primer)
print('сгенерировали случайный словарь :', type_dict_random)
# т.к. ключи не могут повторятся, а цикл идет всего один проход,то каждый повторяющийся ключ будет перезаписываться с новым знчением
print(len(type_dict_random))

## сравнение is,==,in
print("оператор is,in,==")
print('is - это сравнение адреса объекта в памяти')
print('in - это поиск значения в итерируемом объекте')
print('== - это сравнение значений')

one = ['hello']
two = ['hello']

print('\nid объекта переменной one', id(one))
print('id объекта переменной two', id(two))

if one == two:
    print('one == two')
if one is two:
    print('one is two')
if one[0] in two:
    print('one in two')

## ищем совпадения ключей словарей из списка и выводим кол-во c помощью in
print('ищем совпадения ключей словарей из списка и выводим кол-во')
# создаем лист запоненый случаными значениями
type_list_random = [random.randrange(0, 50) for i in range(0, 50)]
# создаем словарь запоненый случаными ключами где True или False это их значения
type_dict_random = {random.randrange(0, 50): random.choice([True, False]) for i in range(0, 10)}
# счетчик подсчета
count = 0
# множество для уникальных значений
set_in_dict = set()
# преобразуем список во множеста для удаление дубликатов
type_set = set(type_list_random)
# смотрим значения
print('все значения словаря:', type_dict_random.keys(), 'в кол-ве:', len(type_dict_random))
print('все значения списка:', type_list_random, 'в кол-ве:', len(type_list_random))
print('уникальные значения множества:', type_set, 'в кол-ве:', len(type_set))
# цикл по ключам словаря, поиск ключа во множестве, добавление в set_in_dict (см. выше), инкремент счетчика
for key in type_dict_random:
    if key in type_set:
        set_in_dict.add(key)
        count = count + 1
        #count += 1
print('совпадений:', count, 'значения', set_in_dict)

## инвертируем тип False и True в словаре c помощью is
# создаем словарь запоненый случаными ключами где True это их значения
type_dict_random = {random.randrange(0, 50): True for i in range(0, 10)}
print('\nнаш словарь до инвертации:', type_dict_random)
for key, value in type_dict_random.items():
    if True is value:
        type_dict_random[key] = False
print('наш словарь после инвертации:', type_dict_random)


## инвертируем тип ['False'] и ['True'] в словаре c помощью ==
# создаем словарь запоненый случаными ключами где ['True'] это их значения
type_dict_random = {random.randrange(0, 50): ['True'] for i in range(0, 10)}
print('наш словарь до инвертации:', type_dict_random)
for key, value in type_dict_random.items():
    #print(id(['True']),id(value))
    if ['True'] == value:
        type_dict_random[key] = ['False']
print('наш словарь после инвертации:', type_dict_random)

## специальные функции lambda,zip,map
# создаем int для примера c lambda
type_int = 5
# создаем лист запоненый случаными значениями из цифр
type_list_random_number = [random.randrange(0, 10) for i in range(0, 10)]
print('\nсгенерировали случайный список чисел :', type_list_random_number)
# создаем лист запоненый случаными булевыми значениями
type_list_random_bool = [random.choice([True, False]) for i in range(0, 10)]
print('сгенерировали случайный список булевых значений :', type_list_random_bool)

# анонимная функция lambda - что-то делает с переменной(первый 'x:') и возвращает результат(после ':')
print('\nlambda')
lambda_func = lambda x: x + 1
print('функция lambda:', lambda_func(type_int))
# простой вариант верхней логики описан ниже
def method_test(x):
    return x + 1
print(method_test(type_int))

# функция zip - объединение двух интерируемых типов в нужный тип
print('\nzip')
type_dict_join_to_lists = dict(zip(type_list_random_number, type_list_random_bool))
print('создали словарь из двух списков:', type_dict_join_to_lists)

type_list_join_to_lists = list(zip(type_list_random_number, type_list_random_bool))
print('создали список с кортежами из двух списков:', type_list_join_to_lists)

type_set_join_to_lists = set(zip(type_list_random_number, type_list_random_bool))
print('создали множество с кортежами из двух списков:', type_set_join_to_lists)

type_tuple_join_to_lists = tuple(zip(type_list_random_number, type_list_random_bool))
print('создали котреж с кортежами из двух списков:', type_tuple_join_to_lists)


# функция map - применяет функцию к каждому элементу списка и возращает новый указаный тип
print('\nmap')
# с использованием string
type_list_map_string = list(map(str, type_list_random_number))
print('сгенерировали случайный список чисел :', type_list_random_number)
print('создаем новый список с использованием map и str:', type_list_map_string)


# с использованием lambda
type_list_map_lambda = list(map(lambda x: x + 1, type_list_random_number))
print('\nсгенерировали случайный список чисел :', type_list_random_number)
print('создаем новый список с использованием map и lambda:', type_list_map_lambda)

# с использованием lambda
type_list_map_method_test = list(map(method_test, type_list_random_number))
print('\nсгенерировали случайный список чисел :', type_list_random_number)
print('создаем новый список с использованием map и method_test:', type_list_map_method_test)
##

