import random
type_list_rand = [str(random.randrange(0, 10)) for i in range(0, 13)]
print(type_list_rand)
type_dict_rand = {random.randrange(0, 25): random.choice([True, False]) for i in range(0, 15)}
print(type_dict_rand)

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
print (type_dict_rand, count)

count = 0
print(set_type_list_rand)
for key in set_type_list_rand:
  if key not in type_dict_rand.keys():
   type_dict_rand[key]= True
   count = count + 1
print (type_dict_rand, count)

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
print (count_1, count_2, count_3)