aList = []
aList.append(1)
aList.append('L')
aList.append(5.7)
aList.append([5, 8, 9])
print(aList, type(aList))

aTuple = (1, 'K', [5, 3.7, 9], {5: 1, 'S': 2, 5.7: 3})
print(aTuple, type(aTuple))

aSet = (3, 'P', [7, 1], {'K': 1, 'S': 2, 7.55: 3})

bTyple = (aList, aTuple)
print(bTyple, type(bTyple))

bTyple[0].pop(-1)
print(bTyple)