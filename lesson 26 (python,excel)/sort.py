##
# Алгоритмы сортировки
# Оценка сложности алгоритмов, или Что такое О(log n)
'''
O(n) — линейная сложность
Такой сложностью обладает, например, алгоритм поиска наибольшего элемента в не отсортированном массиве.
Нам придётся пройтись по всем n элементам массива, чтобы понять, какой из них максимальный.

O(log n) — логарифмическая сложность
Простейший пример — бинарный поиск. Если массив отсортирован, мы можем проверить, есть ли в нём какое-то конкретное значение, методом деления пополам.
Проверим средний элемент, если он больше искомого, то отбросим вторую половину массива — там его точно нет.
Если же меньше, то наоборот — отбросим начальную половину. И так будем продолжать делить пополам, в итоге проверим log n элементов.

O(n2) — квадратичная сложность
Такую сложность имеет, например, алгоритм сортировки вставками.
В канонической реализации он представляет из себя два вложенных цикла: один, чтобы проходить по всему массиву, а второй, чтобы находить место очередному элементу в уже отсортированной части.
Таким образом, количество операций будет зависеть от размера массива как n * n, т. е. n2.
'''

## Пузырьковая сортировка
# Если взять самый худший случай (изначально список отсортирован по убыванию), затраты времени будут равны O(n²), где n — количество элементов списка.
import time
st = time.time()
spis = [2,4,7,8,5,6]
def bubble_sort_alg(spis):
    flg = True
    while flg:
        flg = False
        for i in range(len(spis) - 1):
            if spis[i] > spis[i+1]:
                spis[i],spis[i+1] = spis[i+1],spis[i]
                flg = True
    return spis

print(bubble_sort_alg(spis))
print("----%.10f----"%(time.time()-st))
## Сортировка выбором
# Затраты времени на сортировку выбором в среднем составляют O(n²), где n — количество элементов списка.
import time

st = time.time()
nums = [2,4,7,8,5,6]

def selection_sort_alg(nums):
    # Значение i соответствует кол-ву отсортированных значений
    for i in range(len(nums)):
        # Исходно считаем наименьшим первый элемент
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(nums)):
               if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    return nums


print(selection_sort_alg(nums))
print("----%.10f----"%(time.time()-st))

## Быстрая сортировка
# Затраты времени на сортировку выбором в среднем составляют O(n log n), где n — количество элементов списка.
import time
import random

st = time.time()

def quick_sort_alg(val):
    if len(val) == 2:
        if val[0] > val[1]:
            return [val[1],val[0]]
        else:
            return val
    elif len(val) == 1:
        return val
    else:
        opr = val[round(len(val)/2)]
        sm = []
        op = []
        bg = []
        for i in val:
            if i < opr:
                sm.append(i)
            elif i == opr:
                op.append(i)
            else :
                bg.append(i)
        if not bg and sm:
            return quick_sort_alg(sm)+op
        if not sm and bg:
             return op + quick_sort_alg(bg)
        if not sm and not bg:
            return op

        return quick_sort_alg(sm)+op+quick_sort_alg(bg)


res = [random.randrange(1, 50, 1) for i in range(70)]
print(res)
print(quick_sort_alg(res))
print("----%.10f----"%(time.time()-st))


## comparison algoritm
import time
import random

def bubble_sort_alg(spis):
    flg = True
    while flg:
        flg = False
        for i in range(len(spis) - 1):
            if spis[i] > spis[i+1]:
                spis[i],spis[i+1] = spis[i+1],spis[i]
                flg = True
    return spis


def selection_sort_alg(nums):
    # Значение i соответствует кол-ву отсортированных значений
    for i in range(len(nums)):
        # Исходно считаем наименьшим первый элемент
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(nums)):
               if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    return nums

def quick_sort_alg(val):
    if len(val) == 2:
        if val[0] > val[1]:
            return [val[1],val[0]]
        else:
            return val
    elif len(val) == 1:
        return val
    else:
        opr = val[round(len(val)/2)]
        sm = []
        op = []
        bg = []
        for i in val:
            if i < opr:
                sm.append(i)
            elif i == opr:
                op.append(i)
            else :
                bg.append(i)
        if not bg and sm:
            return quick_sort_alg(sm)+op
        if not sm and bg:
             return op + quick_sort_alg(bg)
        if not sm and not bg:
            return op

        return quick_sort_alg(sm)+op+quick_sort_alg(bg)


res = [random.randrange(1, 50000, 1) for i in range(5000)]
print(res[0:10],'\n')

st = time.time()
print(quick_sort_alg(res)[0:10])
print('Quicksort',"----%.13f----"%(time.time()-st),'\n')

st = time.time()
print(bubble_sort_alg(res)[0:10])
print('Bubble',"----%.13f----"%(time.time()-st),'\n')

st = time.time()
print(selection_sort_alg(res)[0:10])
print('Selection',"----%.13f----"%(time.time()-st),'\n')

st = time.time()
print(sorted(res)[0:10])
print('PythonSort',"----%.13f----"%(time.time()-st),'\n')

print('end')

