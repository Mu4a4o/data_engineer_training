import random
# Денис
## 1
"""
1. Требуется сгенерировать словарь(type_dict_rand) и список(type_list_rand),до 15 элементов в каждой переменной.
В списке должны быть числа типа str.
В словаре в качестве ключа должны быть числа типа int,а в качестве значений True/False (тип bool и тоже определяются рандомом)
"""
type_list_rand = {random.randrange(0, 20) for i in range(0, 15)}
type_dict_rand = {random.randrange(0, 20): random.choice([True, False]) for i in range(0, 15)}
print(type_list_rand)
print(type_dict_rand)
## 2
"""
2. Сделать цикл и условную конструкцию которая ищет одинаковые числа в type_dict_rand и type_list_rand (не забываем про
преобразование str в int или наоборот при их поиске).В случае совпадений, 
требуется изменить в type_dict_rand по ключу True на ['False'] и False на 'True', а так-же
подсчитать кол-во совпадений и вывести после цикла принтом.
"""
count_2 = 0
for key, value in type_dict_rand.items():
    if key in type_list_rand:
        if True is value:
            type_dict_rand[key] = ['False']
            count_2 += 1
        elif False is value:
            type_dict_rand[key] = 'True'
            count_2 += 1
print(count_2)
print(type_dict_rand)
## 3
"""
3. Сделать следующий цикл, который добавит в type_dict_rand те числа, что не были найдены во 2 пункте ,а так-же
подсчитать их кол-во  и вывести после цикла принтом.
Ключ это число типа int, а значением будет True тип bool.
!!! Подсказка т.к я не я не объяснял вам про "не были найдены",можно вместо is, in, == использовать is not, not in, != 
"""
count_3 = 0
for key, value in type_dict_rand.items():
    if key not in type_list_rand:
        type_dict_rand[key] = True
        count_3 += 1
print(count_3)
print(type_dict_rand)
## 4
"""
4. Подсчитать циклом и  условной конструкцией  сколько в type_dict_rand у нас значений и вывести тремя принтами после цикла :
    1. ['False'] типа list[str]
    2. 'True' типа str
    3. True типа bool
"""
count_4 = [0,0,0]
for value in type_dict_rand.values():
    if ['False'] == value:
        count_4[0] += 1
    elif 'True' == value:
        count_4[1] += 1
    elif True is value:
        count_4[2] += 1
print(type_dict_rand.values())
print("['False']", count_4[0])
print("'True'", count_4[1])
print("True", count_4[2])

### Софья
import random
## 1
"""
1. Требуется сгенерировать словарь(type_dict_rand) и список(type_list_rand),до 15 элементов в каждой переменной.
В списке должны быть числа типа str.
В словаре в качестве ключа должны быть числа типа int,а в качестве значений True/False (тип bool и тоже определяются рандомом)
"""
type_list_rand = [str(random.randrange(0, 10)) for i in range(0, 13)]
print(type_list_rand)
type_dict_rand = {random.randrange(0, 25): random.choice([True, False]) for i in range(0, 15)}
print(type_dict_rand)

## 2
"""
2. Сделать цикл и условную конструкцию которая ищет одинаковые числа в type_dict_rand и type_list_rand (не забываем про
преобразование str в int или наоборот при их поиске).В случае совпадений, 
требуется изменить в type_dict_rand по ключу True на ['False'] и False на 'True', а так-же
подсчитать кол-во совпадений и вывести после цикла принтом.
"""
set_type_list_rand = set(map(int, type_list_rand))
count = 0
print(set_type_list_rand)
for key, value in type_dict_rand.items():
    if key in set_type_list_rand and True is value:
        count = count + 1
        type_dict_rand[key] = ['False']
    elif key in set_type_list_rand and False is value:
        count = count + 1
        type_dict_rand[key] = 'True'
print(type_dict_rand, count)

## 3
"""
3. Сделать следующий цикл, который добавит в type_dict_rand те числа, что не были найдены во 2 пункте ,а так-же
подсчитать их кол-во  и вывести после цикла принтом.
Ключ это число типа int, а значением будет True тип bool.
!!! Подсказка т.к я не я не объяснял вам про "не были найдены",можно вместо is, in, == использовать is not, not in, != 
"""
count = 0
print(set_type_list_rand)
for key in set_type_list_rand:
    if key not in type_dict_rand.keys():
        type_dict_rand[key] = True
        count = count + 1
print(type_dict_rand, count)

## 4
"""
4. Подсчитать циклом и  условной конструкцией  сколько в type_dict_rand у нас значений и вывести тремя принтами после цикла :
    1. ['False'] типа list[str]
    2. 'True' типа str
    3. True типа bool
"""
count_1 = 0
count_2 = 0
count_3 = 0
for key, value in type_dict_rand.items():
    if ['False'] == value:
        count_1 = count_1 + 1
    elif 'True' is value:
        count_2 = count_2 + 1
    elif True is value:
        count_3 = count_3 + 1
print(count_1, count_2, count_3)


### Оля и Максим
import  random

"""
1. Требуется сгенерировать словарь(type_dict_rand) и список(type_list_rand),до 15 элементов в каждой переменной.
В списке должны быть числа типа str.
В словаре в качестве ключа должны быть числа типа int,
а в качестве значений True/False (тип bool и тоже определяются рандомом)
"""
type_list_random = [str(random.randrange(0, 20)) for i in range(0, 15)]
type_dict_random = {random.randrange(0, 20): random.choice([True, False]) for i in range(0, 15)}
print(type_list_random)
print(type_dict_random)



"""
2. Сделать цикл и условную конструкцию которая ищет одинаковые числа в type_dict_rand и type_list_rand (не забываем про
преобразование str в int или наоборот при их поиске).В случае совпадений, 
требуется изменить в type_dict_rand по ключу True на ['False'] и False на 'True', а так-же
подсчитать кол-во совпадений и вывести после цикла принтом.
"""
count = 0
for key in type_dict_random:
    for x in type_list_random:
        if int(x) == key:
            count += 1
            if  type_dict_random[key] == False:
                type_dict_random[key] = 'True'
            else:
                type_dict_random[key] = ['False']
print(count)
print(type_dict_random)

"""
3. Сделать следующий цикл, который добавит в type_dict_rand те числа, что не были найдены во 2 пункте ,а так-же
подсчитать их кол-во  и вывести после цикла принтом.
Ключ это число типа int, а значением будет True тип bool.
!!! Подсказка т.к я не я не объяснял вам про "не были найдены",можно вместо is, in, == использовать is not, not in, != 
"""
count_2_1 = 0
for x in type_list_random:
    if int(x) not in type_dict_random:
            count_2_1 += 1
            type_dict_random[int(x)] = True
print(count_2_1)
print(type_dict_random)

"""
4. Подсчитать циклом и  условной конструкцией  сколько в type_dict_rand у нас значений и вывести тремя принтами после цикла :
    1. ['False'] типа list[str]
    2. 'True' типа str
    3. True типа bool
    4. False типа bool
"""
count = [0, 0, 0, 0]
for key in type_dict_random:
    if ['False'] == type_dict_random[key]:
        count[0] += 1
    elif 'True' == type_dict_random[key]:
        count[1] += 1
    elif type_dict_random[key] is True:
        count[2] += 1
    else:
        count[3] += 1
print(count)


###ЧАСТЬ 2 ЗАКРЕПЛЕНИЕ
# Денис
"""1. Требуется сгенерировать словарь type_dict_rand.Ключами будут рандомные str числа.
В качестве значений у каждого ключа будет сгенерированный рандомный список состоящи из int чисел.
Ключей будет 15 шт.
Значений в каждом списке ключа будет тоже 15 шт.
Пример {'1': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],'2':[1,2,3....}
"""
type_dict_rand = {str(random.randrange(0, 15)) : [random.randrange(0, 15) for i in range(0, 15)] for i in range(0, 15)}
print(type_dict_rand)
for key, value in type_dict_rand.items():
    print(key, value)
"""
2.Создать пустой словарь type_dict_count_value. Сделать цикл или циклы, где:
Ключами будут числа, которые есть в значениях списков в словаре type_dict_rand
А значениями ключей будет кол-во найденых чисел во всем словаре type_dict_rand по всем спискам
Пример
Есть словарь type_dict_rand {'5': [1,1,2,10],'1': [5,1,2,100]}
В итоге в type_dict_count_value должно быть { 1 : 3, 2: 2, 10: 1, 100: 1}
"""
type_dict_count_value = {}
for value in type_dict_rand.values():
    for i in value:
        if i in type_dict_count_value:
            type_dict_count_value[i] += 1
        else:
            type_dict_count_value[i] = 1
print(type_dict_count_value)

"""
3.Взять ключи из словаря type_dict_rand и сравнить с ключами type_dict_count_value.
В случае совпадения сделать инкремент значения ключа в type_dict_count_value
Пример
type_dict_rand {'5': [1,1,2,10],'1': [5,1,2,100]}
type_dict_count_value { 1 : 3, 2: 2, 10: 1, 100: 1}
После цикла будет так
type_dict_count_value { 1 : 4, 2: 2, 10: 1, 100: 1}
"""
for key in type_dict_rand:
    if int(key) in type_dict_count_value:
        type_dict_count_value[int(key)] += 1
print(type_dict_count_value)

## Софья
"""
1. Требуется сгенерировать словарь type_dict_rand.Ключами будут рандомные str числа.
В качестве значений у каждого ключа будет сгенерированный рандомный список состоящи из int чисел.
Ключей будет 15 шт.
Значений в каждом списке ключа будет тоже 15 шт.
Пример {'1': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],'2':[1,2,3....}
"""
import random
type_dict_rand = {str(random.randrange(0, 25)):  [random.randrange(0, 25) for i in range(0, 15)] for j in range(0, 15)}
for key, value in type_dict_rand.items():
    print(key, value)

"""
2.Создать пустой словарь type_dict_count_value. Сделать цикл, где:
Ключами будут числа, которые есть в значениях списков в словаре type_dict_rand
А значениями ключей будет кол-во найденых чисел во всем словаре type_dict_rand по всем спискам
Пример
Есть словарь type_dict_rand {'5': [1,1,2,10],'1': [5,1,2,100]}
В итоге в type_dict_count_value должно быть { 1 : 3, 2: 2, 10: 1, 100: 1}
"""
# способ 1
# type_dict_count_value = {}
# list_1 = []
# for key in type_dict_rand:
#     for i in range(len(type_dict_rand[key])):
#      list_1.append(type_dict_rand[key][i])
# print(list_1)
# for i in range(len(list_1)):
#     count = 0
#     for j in range(len(list_1)):
#         if list_1[i] == list_1[j]:
#             count = count+1
#     type_dict_count_value[list_1[i]] = count
# print(type_dict_count_value)

# способ 2
type_dict_count_value = {}
for i in type_dict_rand:
    for j in range(len(type_dict_rand[i])):
        count = 0
        for key in type_dict_rand:
            for x in range(len(type_dict_rand[key])):
             if type_dict_rand[i][j] == type_dict_rand[key][x]:
              count = count+1
        type_dict_count_value[type_dict_rand[i][j]] = count
print(type_dict_count_value)


"""
3.Взять ключи из словаря type_dict_rand и сравнить с ключами type_dict_count_value.
В случае совпадения сделать инкремент значения ключа в type_dict_count_value
Пример
type_dict_rand {'5': [1,1,2,10],'1': [5,1,2,100]}
type_dict_count_value { 1 : 3, 2: 2, 10: 1, 100: 1}
После цикла будет так
type_dict_count_value { 1 : 4, 2: 2, 10: 1, 100: 1}
"""
for key, value in type_dict_count_value.items():
    for i in type_dict_rand:
        if int(i) == key:
            type_dict_count_value[key] = type_dict_count_value[key]+1
print(type_dict_count_value)


## Максим
"""
1. Требуется сгенерировать словарь type_dict_rand.Ключами будут рандомные str числа.
В качестве значений у каждого ключа будет сгенерированный рандомный список состоящи из int чисел.
Ключей будет 15 шт.
Значений в каждом списке ключа будет тоже 15 шт.
Пример {'1': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],'2':[1,2,3....}
"""

import random
type_dict_rand = {random.randrange(0, 15): [random.randrange(0, 15) for i in range(0, 3)] for j in range(0, 3)}
print(type_dict_rand)



"""
2.Создать пустой словарь type_dict_count_value. Сделать цикл, где:
Ключами будут числа, которые есть в значениях списков в словаре type_dict_rand
А значениями ключей будет кол-во найденых чисел во всем словаре type_dict_rand по всем спискам
Пример
Есть словарь type_dict_rand {'5': [1,1,2,10],'1': [5,1,2,100]}
В итоге в type_dict_count_value должно быть { 1 : 3, 2: 2, 10: 1, 100: 1}
"""
type_dict_count_value={}
for value in type_dict_rand.values():
    for i in value:
        if i in type_dict_count_value:
            type_dict_count_value[i] += 1
        else:
            type_dict_count_value[i] = 1
print(type_dict_count_value)

"""
3.Взять ключи из словаря type_dict_rand и сравнить с ключами type_dict_count_value.
В случае совпадения сделать инкремент значения ключа в type_dict_count_value
Пример
type_dict_rand {'5': [1,1,2,10],'1': [5,1,2,100]}
type_dict_count_value { 1 : 3, 2: 2, 10: 1, 100: 1}
После цикла будет так
type_dict_count_value { 1 : 4, 2: 2, 10: 1, 100: 1}
"""
count = 0

for key in type_dict_count_value:
    for x in type_dict_rand:
        if x == key:
            type_dict_count_value[x] += 1
print(type_dict_count_value)

"""
for key in type_dict_rand:
    if int(key) in type_dict_count_value:
        type_dict_count_value[int(key)] += 1
print(type_dict_count_value)
"""