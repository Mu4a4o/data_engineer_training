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

def rec_sort_alg(val):
    if len(val) == 2:
        if val[0] > val[1]:
            return [val[1],val[0]]
        else:
            return val
    elif len(val) == 1:
        return val
    else:
        opr = val[round(len(val)/2)-1]
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
        #print(val,'val')
        #print(sm,'sm')
        #print(op,'op')
        #print(bg,'bg')
        if not bg and sm:
            return rec_sort_alg(sm)+op
        if not sm and bg:
             return op + rec_sort_alg(bg)
        if not sm and not bg:
            return op
        return rec_sort_alg(sm)+op+rec_sort_alg(bg)


res = [random.randrange(1, 50, 1) for i in range(70)]
print(res)
print(rec_sort_alg(res))
print("----%.10f----"%(time.time()-st))


## comparison algoritm
res = [random.randrange(1, 5000, 1) for i in range(500)]
print(res)

st = time.time()
print(bubble_sort_alg(res))
print("----%.13f----"%(time.time()-st))

st = time.time()
print(selection_sort_alg(res))
print("----%.13f----"%(time.time()-st))

st = time.time()
print(rec_sort_alg(res))
print("----%.13f----"%(time.time()-st))

## CHECK
a = [31, 45, 30, 39, 22, 39, 22, 11, 10, 14, 35, 25, 37, 34, 9, 33, 6, 38, 11, 8, 13, 33, 29, 1, 33, 4, 1, 40, 49, 6, 48, 5, 34, 22, 17, 48, 27, 29, 46, 6, 2, 37, 36, 30, 9, 33, 25, 22, 12, 7, 27, 25, 6, 44, 29, 19, 42, 31, 31, 49, 36, 13, 23, 42, 44, 6, 17, 18, 30, 49]
a = sorted(a)
print(a)
c = [1, 1, 2, 4, 5, 6, 6, 6, 6, 6, 7, 8, 9, 9, 10, 11, 11, 12, 13, 13, 14, 17, 17, 18, 19, 22, 22, 22, 22, 23, 25, 25, 25, 27, 27, 29, 29, 29, 30, 30, 30, 31, 31, 31, 33, 33, 33, 33, 34, 34, 35, 36, 36, 37, 37, 38, 39, 39, 40, 42, 42, 44, 44, 45, 46, 48, 48, 49, 49, 49]
b = [1, 1, 2, 4, 5, 6, 6, 6, 6, 6, 7, 8, 9, 9, 10, 11, 11, 12, 13, 13, 14, 17, 17, 18, 19, 22, 22, 22, 22, 23, 25, 25, 25, 27, 27, 29, 29, 29, 30, 30, 30, 31, 31, 31, 33, 33, 33, 33, 34, 34, 35, 36, 36, 37, 37, 38, 39, 39, 40, 42, 42, 44, 44, 45, 46, 48, 48, 49, 49, 49]
print(c == b)