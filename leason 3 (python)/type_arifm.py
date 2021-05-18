""" 18.05.2021 УСЛОВНЫЕ КОНСТРУКЦИИ И ЦИКЛЫ """
#### УСЛОВНЫЕ КОНСТРУКЦИИ
print('УСЛОВНЫЕ КОНСТРУКЦИИ')
print('операторы <,>,==,!=')
a = 1.0
b = 2.0

if a < b:
    print('"а" меньше(<) "b"')
elif a == b:
    print('"а" равно(==) "b"')
elif a != b:
    print('"а" НЕравно(!=) "b"')
else:
    print('"a" больше "b"')
print('\n')

print("оператор is и in")
print('is - это сравнение адреса объекта в памяти')
print('in - это поиск значения в итерируемом объекте')
a = 1
b = 1
c = "1"
d = [1, 0]

if a is b:
    print('"a" is "b"', id(a), id(b))
if a is c:
    print('"a" is "c"')
if a in d:
    print('"a" in "d"')

# for i in type_set:
#     print('type_set =', i)
# print('\n\n')
# for i in type_list:
#     print('type_list =', i)
# print('\n\n')
# for i in type_dict:
#     print('type_dict =', i)
# print('\n\n')


