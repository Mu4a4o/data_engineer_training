'''
1. Реализовать алгоритм сортировки выбором. Я это не объяснял, но задача преследует следующие цели :
    1. Гугление. Самостоятельный поиск объяснения логики алгоритма, т.е  не готовую реализацию в виде кода !!!
    3. Переформатирования мозга. При встрече, мне нужно объяснить код алгоритма, то как ты его понимаешь.
    3. Циклы и условные конструкции. Решаем вопрос с пониманием циклов и условиях.
2. Алгоритм пузырьковой сортировки упаковать в функцию bubble_def, которая обернута в декоратор decor_def,
    который считает время выполнения bubble_def и выводит информацию в файл start_end.txt.
    bubble_def принимает на вход произвольный список СПИСКОВ В КОТОРЫХ ПРОИЗВОЛЬНОЕ КОЛ-ВО ЭЛЕМЕНТОВ ТИПА int.
    [[4,1...n],[6,4,3...n]...n]
    Возращает отсортированЫЕ спискИ.
    [[1,4...n],[3,4,6...n]...n]
3. Алгоритм пузырьковой сортировки тоже переделать под списки списков, для сравнения скорости двух алгоритмов (пузырьковой и выбором)
4. Паш, тебе +  SQL задание доделать.
'''
# Софья
##Задание 1 сортировка с выбором Способ 1:
import random
n = 10
list_1 = [random.randrange(0, 50) for i in range(0, n)]
print(list_1)
for i in range(len(list_1)):
    k = i
    for j in range(i+1, len(list_1)):
        if list_1[j] < list_1[k]:
            k = j
    list_1[k], list_1[i] = list_1[i], list_1[k]
print(list_1)

##Способ 2:
import random
n = 10
list_1 = [random.randrange(0, 50) for i in range(0, n)]
print(list_1)
p = 0
for j in range(len(list_1)):
    m = 1000
    for i in range(p, len(list_1)):
        if list_1[i] < m:
            m = list_1[i]
            k = i
    list_1[k], list_1[j] = list_1[j], list_1[k]
    p = p + 1
print(list_1)

##Задание 2:
import random
import time
import sys
file = 'C:/Users/SoVYakovleva/Desktop/Python_lessons/file.txt'

def decor_def(user_func):
    def fun(*args):
        first_time = time.time()
        sys.stdout = open(file, 'a')
        a = user_func(*args)
        print('difference', time.time() - first_time)
        print(a)
        sys.stdout.close()
        return a
    return fun

@decor_def
def bubble_def(list_1):
    print(list_1)
    for i in range(len(list_1)):
        for j in range(len(list_1[i])-1):
            for k in range(len(list_1[i])-1):
                if list_1[i][k] > list_1[i][k+1]:
                    list_1[i][k], list_1[i][k+1] = list_1[i][k+1], list_1[i][k]
    return list_1
n = 10
list_1 = [[random.randrange(0, 50) for i in range(0, n)] for j in range(0, n)]
bubble_def(list_1)

##Задание 3:
import random
import time
import sys
file = 'C:/Users/SoVYakovleva/Desktop/Python_lessons/file.txt'

def decor_def(user_func):
    def fun(*args):
        first_time = time.time()
        sys.stdout = open(file, 'a')
        a = user_func(*args)
        print('difference', time.time() - first_time)
        print(a)
        sys.stdout.close()
        return a
    return fun

@decor_def
def bubble_def(list_1):
    print('bubble', list_1)
    for i in range(len(list_1)):
        for j in range(len(list_1[i])-1):
            for k in range(len(list_1[i])-1):
                if list_1[i][k] > list_1[i][k+1]:
                    list_1[i][k], list_1[i][k+1] = list_1[i][k+1], list_1[i][k]
    return list_1

@decor_def
def choice_def(list_1):
    print('choice', list_1)
    for i in range(len(list_1)):
        for j in range(len(list_1[i])):
            m = j
            for k in range(j+1, len(list_1[i])):
                if list_1[i][k] < list_1[i][m]:
                    m = k
            list_1[i][m], list_1[i][j] = list_1[i][j], list_1[i][m]
    return list_1

n = 20
list_1 = [[random.randrange(0, 50) for i in range(0, n)] for j in range(0, n)]
bubble_def(list_1)
choice_def(list_1)


# Макс
"""
1. Реализовать алгоритм сортировки выбором. Я это не объяснял, но задача преследует следующие цели :
1. Гугление. Самостоятельный поиск объяснения логики алгоритма, т.е  не готовую реализацию в виде кода !!!
3. Переформатирования мозга. При встрече, мне нужно объяснить код алгоритма, то как ты его понимаешь.
3. Циклы и условные конструкции. Решаем вопрос с пониманием циклов и условиях.
"""
##
def select_def(v_list):
    for k in range (len(v_list)):
        for i in range(len(v_list[k]) - 1):
            m = i
            j = i + 1
            while j < len(v_list[k]):
                if v_list[k][j] < v_list[k][m]:
                    m = j
                j = j + 1
            v_list[k][i], v_list[k][m] = v_list[k][m], v_list[k][i]
    return v_list
t = [[80, 99, 41, 58, 7, 4, 14],[34, 99, 71, 3, 5, 4, 59]]
print(select_def(t))

"""
2. Алгоритм пузырьковой сортировки упаковать в функцию bubble_def, которая обернута в декоратор decor_def,
    который считает время выполнения bubble_def и выводит информацию в файл start_end.txt.
    bubble_def принимает на вход произвольный список СПИСКОВ В КОТОРЫХ ПРОИЗВОЛЬНОЕ КОЛ-ВО ЭЛЕМЕНТОВ ТИПА int.
    [[4,1...n],[6,4,3...n]...n]
    Возращает отсортированЫЕ спискИ.
    [[1,4...n],[3,4,6...n]...n]
"""
##
import time
import sys
path_log = 'C:/Users/NorM/Desktop/dz/start_end.txt'

def decor_def(user_func):
    def wrapp(arg):
        first_time = time.time()
        sys.stdout = open(path_log, 'a')
        #print('запоминам текущее время в first_time', first_time)
        a = user_func(arg)
        print('start_end', time.time() - first_time)
        print(a)
        sys.stdout.close()
        return a
    return wrapp


@decor_def
def bubble_def(p_list):
    print(p_list)
    for k in range (len(p_list)):
        for i in range (len(p_list[k])-1):
            for j in range(len(p_list[k])-1-i):
                if p_list[k][j]>p_list[k][j+1]:
                    p_list[k][j],p_list[k][j+1]=p_list[k][j+1],p_list[k][j]
    return p_list

p_list=[[8,3,7,6,5,4,9,2,1],[8,3,7,6,5,4,9,2,1]]
bubble_def(p_list)

"""
3. Алгоритм пузырьковой сортировки тоже переделать под списки списков, для сравнения скорости двух алгоритмов (пузырьковой и выбором)
"""

import time
import sys
path_log = 'C:/Users/NorM/Desktop/dz/start_end.txt'


def decor_def(user_func):
    def wrapp(arg):
        first_time = time.time()
        sys.stdout = open(path_log, 'a')
        #print('запоминам текущее время в first_time', first_time)
        b = user_func(arg)
        print('start_end', time.time() - first_time)
        print(b)
        sys.stdout.close()
        return b
    return wrapp

@decor_def
def select_def(v_list):
    for k in range (len(v_list)):
        for i in range(len(v_list[k]) - 1):
            m = i
            j = i + 1
            while j < len(v_list[k]):
                if v_list[k][j] < v_list[k][m]:
                    m = j
                j = j + 1
            v_list[k][i], v_list[k][m] = v_list[k][m], v_list[k][i]
    return v_list

t = [[80, 99, 41, 58, 7, 4, 14],[34, 99, 71, 3, 5, 4, 59]]
select_def(t)

