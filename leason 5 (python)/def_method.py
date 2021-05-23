""" 25.05.2021 МЕТОДЫ И ФУНКЦИИ  """
#### МЕТОДЫ И ФУНКЦИИ
import random

print('МЕТОДЫ И ФУНКЦИИ')

print('МЕТОД')
print('Метод вызывается у объекта и взаимодействует с ним', 'object.method()')
type_list_rand = [random.randrange(0, 20) for i in range(0, 15)]
# ниже метод object.append
type_list_rand.append('пример')
print("метод .append: ", type_list_rand)

print('\nФУНКЦИИ')
print('Функция получает аргументы и что-то делает с ними', 'function(argument)')
# ниже две функции print(argument) и len(argument)
print(len(type_list_rand))

## Пользовательские функции
print('\nПростая пользовательская функция')


def user_func(x):
    y = x + 1
    return y


a = 1
b = user_func(1)

print('пример функции user_func(1):', b)
print("""def user_func(x):
    y = 1(x) + 1
    return 2(y)
""")

## Аргументы функции
print('\nПростые аргументы функции и дефолтные')


def user_func(x, y=1):
    z = x + y + 1
    return z


a = 1

b = user_func(1)
print('\nпример функции user_func(1):', b)
print("""def user_func(x, y=1):
    z = 1(x) + 1(y) + 1
    return 3(z)
""")

c = user_func(1, 5)
print('\nпример функции user_func(1, 5):', c)
print("""def user_func(x, y=1):
    z = 1(x) + 5(y) + 1
    return 7(z)
""")


## Функция без возврата
print('\nФункция без возврата и запуск python функции print()')


def user_func(x, y=1):
    z = x + y + 1
    print('пример функции user_func(1) без возврата: ', z)


a = 1

user_func(1)

print("""def user_func(x, y=1):
    z = 1(x) + 1(y) + 1
     print('пример функции user_func(1) без возврата: ', z)
""")

## Функция и более сложные типы
print('\nФункция и болеесложные типы')


def user_func(x, mutable_list_obj=[]):
    mutable_list_obj.append(x)
    print('пример функции user_func(x, mutable_list_obj) print() и c возвратом: ', mutable_list_obj)
    return mutable_list_obj


type_list = user_func(1)
user_func(2, type_list)
user_func(3, type_list)

print('получили на выходе list: ', type_list)

## Функция и произвольное количество аргументов *args (назвать можете как угодно, главное "*")
print('\nФункция и произвольное количество аргументов')
print('!!!!!назвать можете как угодно, главное "*"')


def user_func_args(*args):
    print('тип *args', type(args), 'выводим список аргументов : ', args)


type_int = 10000
type_list = [random.randrange(0, 100) for i in range(0, 10)]
type_str = 'пример'
print('\nвыводим тип *args и его объекты')
user_func_args(type_int, type_list, type_str)


def user_func_args_mod(*args):
    print('выводим первый аргемент : ', args[0])
    print('выводим последний аргемент : ', args[-1])


print('\nвыводим первый и последний аргумент')
user_func_args_mod(type_int, type_list, type_str)

## Функция и произвольное количество ИМЕНОВАННЫХ аргументов **kwargs (назвать можете как угодно, главное "**")
print('\nФункция и произвольное количество ИМЕНОВАННЫХ аргументов c циклом и условием')
print('!!!!!назвать можете как угодно, главное "**"')


def user_func_kwargs(**vegetables):
    print('тип **vegetables', type(vegetables),'выводим список именнованных аргументов :', vegetables)
    for vegetable, amount in vegetables.items():
        if 'potato' == vegetable:
            print('овощь:', f'{vegetable} (картоха), кол-во', amount)
        elif 'tomato' == vegetable:
            print('овощь:', f'{vegetable} (мистер помидор), кол-во', amount)
        elif 'cucumber' == vegetable:
            print('овощь:', f'{vegetable} (огуречик), кол-во', amount)


print('\nвыводим тип **kwargs,его ключи со значениями')
user_func_kwargs(potato=10, tomato=5, cucumber=20)

