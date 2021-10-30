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