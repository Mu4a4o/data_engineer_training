## 1. Требуется сгенерировать словарь(type_dict_rand) и список(type_list_rand),до 15 элементов в каждой переменной.
# В списке должны быть числа типа str.
# В словаре в качестве ключа должны быть числа типа int,а в качестве значений True/False (тип bool и тоже определяются рандомом).
import random
type_list_rand=[random.randrange(0,15) for i in range(0,15)]
for j in type_list_rand:
    j=str(j)
type_dict_random = {random.randrange(0, 15): random.choice([True,False]) for i in range(0,15)}
print(type_list_rand, '\nв списке числа типа:', type(j))
print(type_dict_random)


## 2. Сделать цикл и условную конструкцию которая ищет одинаковые числа в type_dict_rand и type_list_rand (не забываем про
# преобразование str в int или наоборот при их поиске) В случае нахождения совпадений, требуется изменить в type_dict_rand по ключу True на ['False'] и False на 'True', а так-же
# подсчитать кол-во совпадений и вывести после цикла принтом.
count=0
c=0
d=0
for j in type_list_rand:
    j=int(j)
for key,value in type_dict_random.items():
if key in type_list_rand:
    count += 1
    if True is value:
        type_dict_random[key] = False
        c+=1
    if False is value:
        type_dict_random[key] = True
        d+=1
print(count,c,d)
print(type_dict_random)

## 3. Сделать следующий цикл, который добавит в type_dict_rand те числа, что не были найдены во 2 пункте ,а так-же
# подсчитать их кол-во  и вывести после цикла принтом.
# Ключ это число типа int, а значением будет True тип bool.
# !!! Подсказка т.к я не я не объяснял вам про "не были найдены",можно вместо is, in, == использовать is not, not in, !=

count_1=0
for n in type_list_rand:
    if n not in type_dict_random.keys():
        type_dict_random[n]=True
        count_1+=1
        print(n)
        print(type(n))
        print(type(type_dict_random[n]))
print(count_1)
print(type_dict_random)


## 4. Подсчитать циклом и  условной конструкцией  сколько в type_dict_rand у нас значений и вывести тремя принтами после цикла :
#     1. ['False'] типа list[str]
#     2. 'True' типа str
#     3. True типа bool
a=0
b=0
c=0
for key,value in type_dict_random.items():
    if ['False'] == value:
        a+=1
    if  'True' == value:
        b+=1
    if True is value:
        c+=1
print(a,b,c)
print(type_dict_random)

# 5. Вы можете сверить свою логику решения с моим исполнением в DZ.py
#
# ЧАСТЬ 2 ЗАКРЕПЛЕНИЕ
## 1. Требуется сгенерировать словарь type_dict_rand.Ключами будут рандомные str числа.
# В качестве значений у каждого ключа будет сгенерированный рандомный список состоящи из int чисел.
# Ключей будет 15 шт.
# Значений в каждом списке ключа будет тоже 15 шт.
# Пример {'1': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],'2':[1,2,3....}
type_dict_rand={str(random.randrange(0,15)):[random.randrange(0,15) for i in range(0,15)] for i in range(0,15)}
print(type_dict_rand)

## 2.Создать пустой словарь type_dict_count_value. Сделать цикл, где:
# Ключами будут числа, которые есть в значениях списков в словаре type_dict_rand
# А значениями ключей будет кол-во найденых чисел во всем словаре type_dict_rand по всем спискам
# Пример
# Есть словарь type_dict_rand {'5': [1,1,2,10],'1': [5,1,2,100]}
# В итоге в type_dict_count_value должно быть { 1 : 3, 2: 2, 10: 1, 100: 1}

# вариант 1
# type_dict_count_value={}
# zn_all=[]
# for value in type_dict_rand.values():
#     for j in value:
#         zn_all.append(j)
# for i in set(zn_all):
#     type_dict_count_value[i]=zn_all.count(i)
# print(zn_all)
# print(type_dict_count_value)

# вариант 2

type_dict_count_value={}
zn_all=[]
for value in type_dict_rand.values():
    for j in value:
        zn_all.append(j)
for i in set(zn_all):
    count=0
    for j in zn_all:
        if i==j:
             count += 1
    type_dict_count_value[i]=count
print(type_dict_count_value)


## 3.Взять ключи из словаря type_dict_rand и сравнить с ключами type_dict_count_value.
# В случае совпадения сделать инкремент значения ключа в type_dict_count_value
# Пример
# type_dict_rand {'5': [1,1,2,10],'1': [5,1,2,100]}
# type_dict_count_value { 1 : 3, 2: 2, 10: 1, 100: 1}
# После цикла будет так
# type_dict_count_value { 1 : 4, 2: 2, 10: 1, 100: 1}
for key,value in type_dict_count_value.items():
    for i,y in type_dict_rand.items():
        if key==int(i):
            value+=1
    type_dict_count_value[key]=value
print(type_dict_count_value)

##

