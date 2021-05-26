import random
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