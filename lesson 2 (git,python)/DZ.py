## Оля
# Задание 1
##Димас Карабас
aList = []
aList.append(8)
aList.extend([1, 'a', 4.3])
aList.append('b')
aList.append([12, 5.7, 'c'])
print('Ответ на задание 1\n','Элементы списка aList:', aList)

# Задание 2
aTuple = (2, 'a', {1: 'z', 2: 3.42, 'l': 6}, [7, 8, 9])
print('Ответ на задание 2\n','Элементы кортежа aTuple:', aTuple)

# Задание 3
aSet = {1, 2, 3, 'a', 5.32}# должен быть тип 'множества', если так, то нельзя добавить индексируемые элементы
print('Ответ на задание 3\n','Множество или кортеж?', aSet)

# Задание 4
bTuple=(aList, aTuple)
print('Ответ на задание 4\n', 'Элементы кортежа aTuple:', bTuple)

# Задание 5
print('Индекс aList в кортеже bTuple -', bTuple.index(aList))
print('Индекс элемента [12, 5.7, "c"] в списке aList:', aList.index([12, 5.7, 'c']))
bTuple[0].pop(5)
print('Ответ на задание 5\n',bTuple)


## Софья
aList = []
aList.append(1)
aList.append('L')
aList.append (5.7)
aList.append ([5, 8, 9])
print(aList, type(aList))

aTuple = (1, 'K', [5, 3.7, 9], {5: 1, 'S': 2, 5.7: 3})
print(aTuple, type(aTuple))

# ?
aSet = (3, 'P', [7, 1], {'K': 1, 'S': 2, 7.55: 3})

bTyple = (aList, aTuple)
print(bTyple, type(bTyple))

bTyple[0].pop(-1)
print(bTyple)
