"""
Создать функцию к примеру "user_func" (название выбираете свое):
1. "user_func" принимает произвольное количество аргументов.
2. Алгротим должен перемножить все аргументы подданые на вход "user_func" , так-же должна быть проверка на тип INT.
3. "user_func" должна вывести резуальтат перемножения в print, а так-же сделать вернуть (return) его.

"user_func" должна быть обернута в ДЕКОРАТОР "user_decor" (название выбираете свое):
1. "user_decor" введет логирование (stdout,stderr) отработки "user_func" и записывает все в файл "user_log" (название выбираете свое)
Для проверки сделайте сознательную ошибку в "user_func"
2. "user_decor" введет подсчет времени выполнения "user_func" и выводит его в print
"""

# Денис
# reduce поможет в перемножении элементов
import sys
import time
import  datetime
from functools import reduce

path_log = 'denis_log.txt'

def user_decor(user_func):
    # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.
    def the_wrapper_around_the_original_function(*args):
        try:
            sys.stdout = open(path_log, 'a')
            first_time = time.time()
            print('start:', datetime.datetime.now())
            a = user_func(*args)  # Сама функция
            print('время исполнения: ', time.time() - first_time)
            print('good:', datetime.datetime.now(), '\n')
            return a
        except Exception as ex:
            sys.stderr = open(path_log, 'a')
            print('bad:', ex, datetime.datetime.now(), '\n')
            sys.stderr.close()
        finally:
            sys.stdout.close()
    # Вернём эту функцию
    return the_wrapper_around_the_original_function


@user_decor
def my_func(*args):
    # проверяем каждый элекмент на int, и возвращаем список проверок в виде False/True
    check_int = list(map(lambda x: isinstance(x, int), args))
    # ошибка для провреки
    #4/0
    # если в списке присутствует постороний тип, то условная конструкция пропускает перемножение
    if False not in check_int:
        multiplier = reduce(lambda x, y: y * x, args)
        print('результат', multiplier)
        return multiplier
    else:
        print('есть посторонний тип')

#my_func(1, 2, 3, '4')
my_func(1, 2, 3, 4)








