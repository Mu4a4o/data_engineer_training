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

print('test')

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