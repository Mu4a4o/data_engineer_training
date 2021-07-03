1)
import random
type_dict_rand = {str(random.randrange(0, 25)):  [random.randrange(0, 25) for i in range(0, 15)] for j in range(0, 15)}
print(type_dict_rand)

2)
способ 1
type_dict_count_value = {}
list_1 = []
for key in type_dict_rand:
    for i in range(len(type_dict_rand[key])):
     list_1.append(type_dict_rand[key][i])
print(list_1)
for i in range(len(list_1)):
    count = 0
    for j in range(len(list_1)):
        if list_1[i] == list_1[j]:
            count = count+1
    type_dict_count_value[list_1[i]] = count
print(type_dict_count_value)

способ 2
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
3)
for key, value in type_dict_count_value.items():
    for i in type_dict_rand:
        if int(i) == key:
            type_dict_count_value[key] = type_dict_count_value[key]+1
print(type_dict_count_value)