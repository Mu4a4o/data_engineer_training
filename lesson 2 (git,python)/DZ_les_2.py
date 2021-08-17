## Оля
# Задание 1
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

## Максим Гончаров
#1. Создать пустой лист "aList". Потом требуеся заполнить его любыми изменяемыми и неизменяемыми объектами на ваше усмотрение.Выведите на экран переменную "aList".
#Общее кол-во объектов в переменной "aList" должно быть до 10 шт. и соотношения типов выбираете сами.
aList=[]
aList.append(9)
aList.append('fat')
aList.append(7.40)
aList.extend([459,'df','76.08',9,'cat','rr',[5,'bb',9.07]])
print(type(aList),aList)

#2. Создать кортеж "aTuple". В нем сразу должны содержаться изменяемые и неизменяемые типы объектов,
#а  так-же один индексируемый,итерируемый,неупорядоченные тип.Выведите на экран переменную "aTuple".
#Общее кол-во объектов в переменной "aTuple" должно быть до 10 шт. и соотношения типов выбираете сами.
aTuple=(459,'df','76.08',9,'cat','rr',{5:'bb',9:'hz'})
print(type(aTuple),aTuple)
#3. Создать множества "aSet". В нем сразу должны содержаться изменяемые и неизменяемые типы объектов, а так-же один индексируемый,итерируемый,неупорядоченные тип (на внимательность).
#Общее кол-во объектов в переменной "aSet" должно быть до 10 шт. и соотношения типов выбираете сами.
aSet={459,'df','76.08',9,'cat','rr',5,'bb',9,7}
aSet.add(44)
aSet.discard(44)
print(type(aSet),aSet)
#4. Создать кортеж "bTuple". В нем сразу должны находится "aList" и "aTuple".Выведите на экран переменную "bTuple".
bTuple=([9, 'fat', 7.4, 459, 'df', '76.08', 9, 'cat', 'rr', [5, 'bb', 9.07]],(459, 'df', '76.08', 9, 'cat', 'rr', [5, 'bb', 9.07]))
print(type(bTuple),bTuple)
#5. Это задание сложное поэтому опциональное. Удалите у "aList" последний элемент,но только через обращение к индексу у кортежа "bTuple" ( см. задание 4,у нас получается два индекса)
#и вывидите на экран "bTuple" в котором будет "aList" без последнего элемента.
bTuple[0].pop()
#bTuple[0].pop(-1)
print(bTuple)