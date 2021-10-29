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
flg = True
while flg:
    flg = False
    for i in range(len(spis) - 1):
        if spis[i] > spis[i+1]:
            spis[i],spis[i+1] = spis[i+1],spis[i]
            flg = True

print(spis)
print("----%.10f----"%(time.time()-st))
## Сортировка выбором
# Затраты времени на сортировку выбором в среднем составляют O(n²), где n — количество элементов списка.
import time

st = time.time()

nums = [2,4,7,8,5,6]

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


print(nums)
print("----%.10f----"%(time.time()-st))


