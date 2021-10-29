'''
ДЗ для Макса
1. Создать переменные типа строка,листа,множенства,словаря,кортежа и обогатить их произвольными данными.

2. Доказать при помощи кода, какие переменные из первой задачи являются immutable,а какие mutable при помощи функции id

3. Реализовать алгоритм пузырьковой сортировки. Я это не объяснял, но задача преследует следующие цели :
    1. Гугление. Самостоятельный поиск объяснения логики алгоритма, т.е  не готовую реализацию в виде кода !!!
    3. Переформатирования мозга. При встрече, мне нужно объяснить код алгоритма, то как ты его понимаешь.
    3. Циклы и условные конструкции. Решаем вопрос с пониманием циклов и условиях.

4. Алгоритм пузырьковой сортировки упаковать в функцию bubble_def, которая обернута в декоратор decor_def,
    который считает время выполнения bubble_def и выводит информацию в файл start_end.txt.
    bubble_def принимает на вход произвольный список чисел (int) и возращает отсортированый список.

'''
## 1. Создать переменные типа строка,листа,множенства,словаря,кортежа и обогатить их произвольными данными.
t_str = 'a,b,c'
print(type(t_str))
t_list = ['a', 8, 9.0]
print(type(t_list))
t_set = {'a', 8, 9.0}
print(type(t_set))
t_dict = {1: 'a', 2: 3, 3: 8.0}
print(type(t_dict))
t_tuple = (9, 'a', 'b', 'c', 4, 7.0)
print(type(t_tuple))

## 2. Доказать при помощи кода, какие переменные из первой задачи являются immutable,а какие mutable при помощи функции id

t_str = 'a,b,c'
print('t_str id', id(t_str))
t_str = 'a,b,c' + 'f'
print('t_str id', id(t_str), '\n')

t_list = ['a', 8, 9.0]
print('t_list id', id(t_list))
t_list.append(8.0)
print('t_list id', id(t_list), '\n')

t_set = {'a', 8, 9.0}
print('t_set id', id(t_set))
t_set.add(9.0)
print('t_set id', id(t_set), '\n')

t_dict = {1: 'a', 2: 3, 3: 8.0}
print('t_dict id', id(t_dict))
t_dict['f'] = 'b'
print('t_dict id', id(t_dict), '\n')

t_tuple = (9, 'a', 'b', 'c', 4, 7.0)
print('t_tuple id', id(t_tuple))
t_tuple = ('a', 'b', 'c')
print('t_tuple id', id(t_tuple), '\n')

##1.
import  datetime
p_list = [8, 3, 7, 6, 5, 4, 9, 2, 1]
a = datetime.datetime.now()
p_list.sort()
print(datetime.datetime.now()-a)

p_list = [8, 3, 7, 6, 5, 4, 9, 2, 1]
a = datetime.datetime.now()
for i in range(len(p_list) - 1):
    for j in range(len(p_list) - 1 - i):
        if p_list[j] > p_list[j + 1]:
            p_list[j], p_list[j + 1] = p_list[j + 1], p_list[j]
        #print(i, j, p_list)
print(datetime.datetime.now()-a)

##4.
import time
import sys

path_log = '/Users/dgribanov/PycharmProjects/data_engineer_training/DZ/start_end.txt'


def decor_def(user_func):
    def wrapp(**args):
        first_time = time.time()
        sys.stdout = open(path_log, 'a')
        # print('запоминам текущее время в first_time', first_time)
        a = user_func(**args)
        print('start_end', time.time() - first_time)
        print(a)
        sys.stdout.close()
        return a

    return wrapp


@decor_def
def bubble_def(p_list):
    print(p_list)
    for i in range(len(p_list) - 1):
        for j in range(len(p_list) - 1 - i):
            if p_list[j] > p_list[j + 1]:
                p_list[j], p_list[j + 1] = p_list[j + 1], p_list[j]
    return p_list


p_list = [8, 3, 7, 6, 5, 4, 9, 2, 1]

bubble_def(p_list)

'''
ДЗ для Паши
1.1 Вывести все поля по subscriber_information.

1.2 Вывести все поля по subscriber_information, где connection_date от '2020.01.15'(вклюительно)

1.3 Вывести connection_date и агрегацию connection_date по кол-ву, где connection_date от '2020.01.15'(не вклюительно)

1.4 Вывести группировку из 1.3 и добавить поля с агрегацией, где указаны максимумы по полю  number_of_tv_devices и number_of_internet_devices

1.5 Вывести кол-во плохих и хороших комментариев по датам подключения.

2.1 Вывести поля subscriber_information(основная) и period_traffic при помощи левого объединения (LJ). Дублирующих полей не должно быть!!!

2.2 Сделать LJ subscriber_information(основная) и period_traffic.
	Вывести поля day и макимумы по полю  traffic_gb (получим самый большой трафик за дату).
    В фильтрах интересуют информация по абонентам, которые были подключены от '2020-01-13'(вклюительно).

2.3 Вывести дату трафика и сам трафик абонентов, которые были подключены позже '2020-01-13'(вклюительно) и были довольны при подключении.

2.4 !!! Вывести кол-во id_abon, которые были не довольны при подключении, а так-же были подключены менее
                     2020-02-15, а только чей трафик
	в промежутке с 2020-02-01(вклюительно) по 2020-02-15(вклюительно) был не более 100 GB. !!!
'''

##
