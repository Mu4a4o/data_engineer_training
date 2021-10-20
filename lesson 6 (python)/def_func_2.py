""" 27.05.2021 ФУНКЦИИ Ч.2  """
#### РЕКУРСИЯ, ДЕКОРАТОРЫ, МОДУЛИ time и datetime
import sys

## Полезные модули и их методы

# import time
print('\nмодуль time')

import time

first_time = time.time()
print('запоминам текущее время в first_time', first_time)

print('ждем 5 секунд')
time.sleep(5)

last_time = time.time()
print('запоминам текущее время в last_time', last_time)

delta_time = last_time - first_time
print('получаем разницу в last_time', delta_time)

## import datetime

import datetime

first_datetime = datetime.datetime.now()
print('запоминам текущую дату в first_time', first_datetime)

print('ждем 5 секунд')
#time.sleep(5)

last_datetime = datetime.datetime.now()
print('запоминам текущее время в last_time', last_datetime)

delta_datetime = last_datetime - first_datetime
print('получаем разницу в last_time', delta_datetime)

print('\nработа с форматированием')

datetime_datetime = datetime.datetime.now()
datetime_to_string = datetime_datetime.strftime('%Y %m %d %H:%M:%S')
print('преобразовываем из типа datetime в строку', datetime_to_string)

string_to_datetime = datetime.datetime.strptime(datetime_to_string, '%Y %m %d %H:%M:%S')
print('преобразовываем из типа строка в datetime', string_to_datetime-datetime.timedelta(days=30))

## Декораторы
import time
def func_decoration(user_func):
    # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.
    def the_wrapper_around_the_original_function(*args):
        first_time = time.time()
        print('запоминам текущее время в first_time', first_time)
        a = user_func(*args)  # Сама функция
        print('получаем разницу', time.time() - first_time)
        return a

    # Вернём эту функцию
    return the_wrapper_around_the_original_function

@func_decoration
def user_func_test(*args):
    x = args[0]
    y = args[1]
    return x + y


def func_decoration_2(user_func):
    # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.
    def the_wrapper_around_the_original_function(x_1, y_2):
        first_time = time.time()
        print('запоминам текущее время в first_time', first_time)
        a = user_func(x_1,y_2)  # Сама функция
        print('получаем разницу', time.time() - first_time)
        return a

    # Вернём эту функцию
    return the_wrapper_around_the_original_function

@func_decoration_2
def user_func_test_2(x_1,y_2):
    x = x_1
    y = y_2
    return x + y


def func_decoration_3(user_func):
    # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.
    def the_wrapper_around_the_original_function():
        first_time = time.time()
        print('запоминам текущее время в first_time', first_time)
        a = user_func()  # Сама функция
        print('получаем разницу', time.time() - first_time)
        return a

    # Вернём эту функцию
    return the_wrapper_around_the_original_function

@func_decoration_3
def user_func_test_3():
    x = 10
    y = 25
    time.sleep(10)
    return x + y


print(user_func_test(1, 2))
print(user_func_test_2(5, 6))
print(user_func_test_3())
## Рекурсия

print('\nПростая пользовательская рекурсия на примере факториала')
'''Факториал числа — это число, умноженное на каждое предыдущее число вплоть до 1.
Например, факториал числа 7:
7! = 7*6*5*4*3*2*1 = 5040
'''

def user_func_factorial(x):
    if x == 1:
        return x
    else:
        return x * user_func_factorial(x - 1)

b = user_func_factorial(3)

print('пример функции user_func_factorial(3):', b)
print("""user_func_factorial(3):
            if 3 == 1:
                return x
            else:
                return 3*user_func_factorial(3-1):
                            if 2 == 1:
                                return x
                            else:
                                return 2*user_func_factorial(2-1):
                                            if 1 == 1:
                                                return 1
          return 3(25 строка) * return 2(29 строка) * return 1(31 строка) 
""")

#print('\nустановление глубины рекурсии (по умолчанию 1000', sys.setrecursionlimit(10000))
print('\nлимит глубины рекурсии', sys.getrecursionlimit())




pr1 pr2
1   10.12.2010
1   10.12.2010
2
3
1   10.10.2010